from django.test import TestCase, Client
import pytest
from django.urls import reverse
from django.contrib.auth.models import User, Permission
from pricing.models import Pricing
from pricing.views import DownloadPDFView
from django.test import RequestFactory
from django.template import Context, Template
from django.http import HttpRequest
from datetime import datetime
from pricing.forms import  PricingForm
from decimal import Decimal


@pytest.fixture
def user_client():
    user = User.objects.create_user(username='testuser', password='testpassword')
    client = Client()
    client.login(username='testuser', password='testpassword')
    
    # Assign all required permissions to the user
    permissions = Permission.objects.filter(content_type__app_label='pricing')
    user.user_permissions.set(permissions)
    
    return client

@pytest.fixture
def pricing_list():
    return [
        Pricing.objects.create(
            service_name="Service 1",
            service_number="123",
            vehicle="Car",
            price=100
        ),
        Pricing.objects.create(
            service_name="Service 2",
            service_number="456",
            vehicle="Motorcycle",
            price=200
        ),
    ]

@pytest.mark.django_db
def test_pricing_list_view(client, pricing_list):
    url = reverse('pricing-list')
    response = client.get(url)
    assert response.status_code == 200
    assert 'Lista Dostępnych Usług' in response.content.decode()
    assert 'Service 1' in response.content.decode()
    assert 'Service 2' in response.content.decode()
    assert '123' in response.content.decode()
    assert '456' in response.content.decode()
    assert 'Car' in response.content.decode()
    assert 'Motorcycle' in response.content.decode()
    assert '100' in response.content.decode()
    assert '200' in response.content.decode()

@pytest.mark.django_db
def test_pricing_list_view_authenticated(user_client, pricing_list):
    url = reverse('pricing-list')
    response = user_client.get(url)
    assert response.status_code == 200
    assert 'Lista Dostępnych Usług' in response.content.decode()
    assert 'Service 1' in response.content.decode()
    assert 'Service 2' in response.content.decode()
    assert '123' in response.content.decode()
    assert '456' in response.content.decode()
    assert 'Car' in response.content.decode()
    assert 'Motorcycle' in response.content.decode()
    assert '100' in response.content.decode()
    assert '200' in response.content.decode()
    assert 'Zalogowany użytkownik: testuser' in response.content.decode()

@pytest.mark.django_db
def test_pricing_list_view_not_authenticated(client, pricing_list):
    url = reverse('pricing-list')
    response = client.get(url)
    assert response.status_code == 200
    assert 'Lista Dostępnych Usług' in response.content.decode()
    assert 'Service 1' in response.content.decode()
    assert 'Service 2' in response.content.decode()
    assert '123' in response.content.decode()
    assert '456' in response.content.decode()
    assert 'Car' in response.content.decode()
    assert 'Motorcycle' in response.content.decode()
    assert '100' in response.content.decode()
    assert '200' in response.content.decode()
    assert 'Zaloguj' in response.content.decode()
    assert 'Nie masz konta?' in response.content.decode()



@pytest.mark.django_db
def test_pricing_create_view(user_client):
    url = reverse('pricing-create')
    data = {
        'service_name': 'New Service',
        'service_number': '789',
        'price': '300',
        'vehicle': 'Truck',
    }
    response = user_client.post(url, data=data)
    assert response.status_code == 302, f"Expected status code 302, but got {response.status_code}"

    created_pricing = Pricing.objects.last()
    print(response.content)  # Print the response content
    print(created_pricing)  # Print the created_pricing object
    assert created_pricing is not None, "Pricing object was not created"
    assert created_pricing.service_name == 'New Service', f"Expected service_name to be 'New Service', but got {created_pricing.service_name}"
    assert created_pricing.service_number == Decimal('789'), f"Expected service_number to be Decimal('789'), but got {created_pricing.service_number}"
    assert created_pricing.price == 300, f"Expected price to be 300, but got {created_pricing.price}"
    assert created_pricing.vehicle == 'Truck', f"Expected vehicle to be 'Truck', but got {created_pricing.vehicle}"



@pytest.mark.django_db
def test_pricing_update_view(user_client):
    pricing = Pricing.objects.create(
        service_name='Test Service',
        service_number='123',
        price='100',
        vehicle='Car',
    )
    url = reverse('pricing-update', kwargs={'pk': pricing.id})
    response = user_client.post(
        url,
        data={
            'service_name': 'Updated Service',
            'service_number': '456',
            'price': '200',
            'vehicle': 'Motorcycle',
        }
    )
    assert response.status_code == 302  # Redirects after successful update
    pricing.refresh_from_db()
    assert pricing.service_name == 'Updated Service'
    assert pricing.service_number == Decimal('456')

    
    
@pytest.fixture
def example_data():
    return {
        'name': 'John',
        'surname': 'Doe',
        'email': 'johndoe@example.com',
        'vehicle': 'Car',
        'services': 'Service 1, Service 2',
        'payment_amount': 100,
        'date': '2023-06-01',
        'payment_method': 'Credit Card',
        'payment_details': 'XXXX-XXXX-XXXX-1234',
    }

@pytest.mark.django_db
def test_download_pdf_template(example_data):
    request = HttpRequest()
    request.method = 'POST'
    request.user = None
    request.session = {}
    request.META = {}
    request.POST = example_data  # Use example_data as the POST data

    view = DownloadPDFView()
    response = view.post(request)

    assert response.status_code == 200
    assert response['Content-Type'] == 'application/pdf'
    assert 'attachment; filename="order_' in response['Content-Disposition']