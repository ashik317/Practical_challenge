# asset_management/tests/test_views.py

from django.test import TestCase, Client
from django.urls import reverse
from .models import Company
from asset_management.views import CompanyListAPIView  # Update the import statement

class CompanyListViewTestCase(TestCase):
    def setUp(self):
        self.company = Company.objects.create(name="Test Company")
        self.url = reverse('company-list')

    def test_company_list_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.company.name)
