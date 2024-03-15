# asset_management/views.py

from rest_framework import generics
from .models import Company, Employee, Device
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import ListView

class MyView(APIView):
    """
    A sample API view for testing authentication.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Responds with a simple message.
        """
        content = {'message': 'Hello, World!'}
        return Response(content)

class CompanyListAPIView(generics.ListCreateAPIView):
    """
    API view for listing and creating companies.
    """

    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a company.
    """

    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class EmployeeListAPIView(generics.ListCreateAPIView):
    """
    API view for listing and creating employees.
    """

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting an employee.
    """

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DeviceListAPIView(generics.ListCreateAPIView):
    """
    API view for listing and creating devices.
    """

    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DeviceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a device.
    """

    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class CompanyListView(ListView):
    """
    HTML rendering view for listing companies.
    """

    model = Company
    template_name = 'company_list.html'  # Update with your template name
    context_object_name = 'companies'
