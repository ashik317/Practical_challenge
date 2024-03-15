# Inside your_app/models.py

from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=100)
    # Add other company-related fields as needed

    def __str__(self):
        return self.name

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    # Add other employee-related fields as needed

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.department}"

class Device(models.Model):
    SERIAL_NUMBER_LENGTH = 50
    CONDITION_CHOICES = [
        ('excellent', 'Excellent'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
    ]

    serial_number = models.CharField(max_length=SERIAL_NUMBER_LENGTH, unique=True)
    model = models.CharField(max_length=100)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    assigned_to = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    assigned_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    # Add other device-related fields as needed

    def __str__(self):
        return f"{self.model} - {self.serial_number}"

# In the models above, we define the Company, Employee, and Device models.
# These models represent the core entities of our asset management system.
# Company represents a company or organization that owns assets.
# Employee represents an employee of a company.
# Device represents a physical asset owned by a company and assigned to an employee.
# We use ForeignKey and OneToOneField to establish relationships between these models.
# The __str__() method is overridden in each model to provide a human-readable representation.