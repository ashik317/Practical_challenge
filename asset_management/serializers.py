from rest_framework import serializers
from .models import Company, Employee, Device

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

# In the serializers above, we define serializers for the Company, Employee, and Device models.
# These serializers specify how model instances should be serialized/deserialized when interacting with the API.
# We use ModelSerializer provided by Django REST Framework for convenience.
# Each serializer includes Meta class with the model and fields attributes to specify the model and fields to be serialized.
