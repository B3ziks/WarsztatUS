import pytest, copy
from django.urls import reverse
from django.contrib.auth.models import User, Permission
from employee.models import Employee, Position
from employee.forms import EmployeeForm
from django.test import TestCase, Client
from django.http import QueryDict
from datetime import datetime

@pytest.fixture
def authenticated_client(client):
    user = User.objects.create_user(username='testuser2', password='testpassword2')
    user.user_permissions.add(Permission.objects.get(codename='view_employee'))
    user.user_permissions.add(Permission.objects.get(codename='add_employee'))
    user.user_permissions.add(Permission.objects.get(codename='change_employee'))
    user.user_permissions.add(Permission.objects.get(codename='delete_employee'))
    client = Client()
    client.login(username='testuser2', password='testpassword2')
    return client

@pytest.mark.django_db
def test_employee_list_view(authenticated_client):
    url = reverse('employee-list')
    response = authenticated_client.get(url)
    assert response.status_code == 200


class EmployeeDetailsViewTest(TestCase):
    def test_employee_details_view(self):
        position = Position.objects.create(name='Manager')
        employee = Employee.objects.create(
            first_name='John',
            last_name='Doe',
            position=position,
            status='h'
        )

        url = reverse('employee-details', kwargs={'pk': employee.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)  # Expecting a redirect

        # Follow the redirect
        redirect_url = response.url
        response = self.client.get(redirect_url)

        self.assertEqual(response.status_code, 200)  # Expecting a direct rendering



class EmployeeCreateViewTest(TestCase):
    def test_employee_create_view(self):
        url = reverse('employee-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect

        position = Position.objects.create(name='Kierownik')

        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'birth_date': '1990-01-01',
            'description': 'Some description',
            'position': position.id,
            'status': 'h',
            'image': '',  # Add an empty string or None for the image field
        }
        form = EmployeeForm(data=form_data)
        self.assertTrue(form.is_valid())

        response = self.client.post(url, data={k: v for k, v in form.cleaned_data.items() if v is not None})
        self.assertEqual(response.status_code, 302)  # Expecting a redirect



class EmployeeUpdateViewTest(TestCase):
    def test_employee_update_view(self):
        position = Position.objects.create(name='Manager')
        employee = Employee.objects.create(
            first_name='John',
            last_name='Does',
            position=position,
            status='h'
        )

        url = reverse('employee-update', kwargs={'pk': employee.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect

        # Follow the redirect
        response = self.client.get(response.url)
        self.assertEqual(response.status_code, 200)  # Expecting a success response

        form_data = {
            'first_name': 'John',
            'last_name': 'Does',  # Update the last name to 'Does'
            'birth_date': '1990-01-01',
            'description': 'Some description',
            'position': position.id,
            'status': 'h',
            'image': '',  # Add an empty string or None for the image field
        }
        form = EmployeeForm(data=form_data)
        self.assertTrue(form.is_valid())

        response = self.client.post(url, data={k: v for k, v in form.cleaned_data.items() if v is not None})
        self.assertEqual(response.status_code, 302)  # Expecting a redirect

        # Assert the updated employee's data
        updated_employee = Employee.objects.get(id=employee.id)
        self.assertEqual(updated_employee.first_name, 'John')
        self.assertEqual(updated_employee.last_name, 'Does')  # Check the last name

        
@pytest.mark.django_db
def test_employee_delete_view(authenticated_client):
    position = Position.objects.create(name='Manager')
    employee = Employee.objects.create(first_name='John', last_name='Doe', position=position, status='h')

    url = reverse('employee-delete', kwargs={'pk': employee.id})
    response = authenticated_client.get(url)
    assert response.status_code == 302  # Redirects after successful deletion
    assert not Employee.objects.filter(id=employee.id).exists()