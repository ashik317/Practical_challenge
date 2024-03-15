from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path, include
from asset_management.views import MyView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('admin/', admin.site.urls),
    path('', include('asset_management.urls')),
    path('api/', include('asset_management.urls')),
]
