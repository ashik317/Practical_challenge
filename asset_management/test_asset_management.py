# asset_management/tests/test_models.py

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Company, Employee, Device

class CompanyModelTestCase(TestCase):
    def setUp(self):
        self.company = Company.objects.create(name="Test Company")

    def test_company_name(self):
        self.assertEqual(str(self.company), "Test Company")

class EmployeeModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', email='test@example.com', password='password')
        self.company = Company.objects.create(name="Test Company")
        self.employee = Employee.objects.create(user=self.user, company=self.company, department="Test Department")

    def test_employee_str(self):
        expected_str = f"{self.user.get_full_name()} - Test Department"
        self.assertEqual(str(self.employee), expected_str)

class DeviceModelTestCase(TestCase):
    def setUp(self):
        self.company = Company.objects.create(name="Test Company")
        self.user = User.objects.create_user(username='test_user', email='test@example.com', password='password')
        self.employee = Employee.objects.create(user=self.user, company=self.company, department="Test Department")
        self.device = Device.objects.create(serial_number="123456789", model="Test Model", condition="excellent", assigned_to=self.employee)

    def test_device_str(self):
        expected_str = "Test Model - 123456789"
        self.assertEqual(str(self.device), expected_str)
