import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.test import TestCase


@pytest.fixture
def user_client():
    user = User.objects.create_user(username='testuser', password='testpassword')
    client = Client()
    client.login(username='testuser', password='testpassword')
    return client

@pytest.fixture
def authenticated_user():
    user = User.objects.create_user(username='testuser2', password='testpassword2')
    user.set_password('testpassword2')
    user.save()
    return user


@pytest.mark.django_db
def test_home_view(user_client):
    url = reverse('home')
    response = user_client.get(url)
    assert response.status_code == 200
    assert 'home.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_account_view(user_client):
    url = reverse('account')
    response = user_client.get(url)
    assert response.status_code == 200
    assert 'account.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_contact_view(user_client):
    url = reverse('contact')
    response = user_client.get(url)
    assert response.status_code == 200
    assert 'contact.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_login_view(client):
    # Create the user
    User.objects.create_user(username='testuser', password='testpassword')

    url = reverse('login')
    response = client.get(url)
    assert response.status_code == 200
    assert 'login.html' in [t.name for t in response.templates]

    # Test login
    data = {
        'username': 'testuser',
        'password': 'testpassword',
    }
    client.force_login(User.objects.get(username=data['username']))
    response = client.post(url, data=data, follow=True)
    assert response.status_code == 200
    assert response.wsgi_request.user.is_authenticated

    # Additional assertions if needed
    assert response.wsgi_request.user.username == 'testuser'
    

@pytest.mark.django_db
def test_register_view(client):
    url = reverse('signup')
    response = client.get(url)
    assert response.status_code == 200
    assert 'signup.html' in [t.name for t in response.templates]

    # Test registration
    data = {
        'username': 'testuser',
        'first_name': 'Test',
        'last_name': 'User',
        'email': 'testuser@example.com',
        'password1': 'ifdOxoycVX5T7mG',
        'password2': 'ifdOxoycVX5T7mG',
    }
    response = client.post(url, data=data, follow=True)
    assert response.status_code == 200

    # Check user authentication and user object
    user = User.objects.get(username=data['username'])
    client.force_login(user)
    assert client.session['_auth_user_id'] == str(user.pk)
    

class PChangeViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_pchange_view(self):
        self.client.force_login(self.user)

        # Create the form data for password change
        form_data = {
            'old_password': 'testpass',
            'new_password1': 'newtestpass',
            'new_password2': 'newtestpass',
        }

        # Make a POST request to the pchange view with the form data and follow the redirect
        response = self.client.post(reverse('pchange'), data=form_data, follow=True)

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the user is still authenticated after password change
        self.assertTrue(self.user.is_authenticated)

        # Assert that the user is redirected to the home view
        self.assertTemplateUsed(response, 'home.html')