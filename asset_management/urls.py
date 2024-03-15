# asset_management/urls.py

from django.urls import path
from . import views

app_name = 'asset_management'

urlpatterns = [
    # HTML rendering URLs
    path('companies/', views.CompanyListView.as_view(), name='company-list'),

    # API URLs
    path('api/companies/', views.CompanyListAPIView.as_view(), name='api-company-list'),
    path('api/companies/<int:pk>/', views.CompanyDetailAPIView.as_view(), name='api-company-detail'),
    path('api/employees/', views.EmployeeListAPIView.as_view(), name='api-employee-list'),
    path('api/employees/<int:pk>/', views.EmployeeDetailAPIView.as_view(), name='api-employee-detail'),
    path('api/devices/', views.DeviceListAPIView.as_view(), name='api-device-list'),
    path('api/devices/<int:pk>/', views.DeviceDetailAPIView.as_view(), name='api-device-detail'),

    # Sample view for testing
    path('hello/', views.MyView.as_view(), name='hello'),
]
