# asset_management/tests/test_serializers.py

from django.test import TestCase
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer
from .models import Company, Employee, Device

class CompanySerializerTestCase(TestCase):
    def test_serializer(self):
        company = Company.objects.create(name="Test Company")
        serializer = CompanySerializer(instance=company)
        self.assertEqual(serializer.data['name'], "Test Company")

# Similarly, you can write tests for EmployeeSerializer and DeviceSerializer
