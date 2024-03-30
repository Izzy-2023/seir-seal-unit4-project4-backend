"""
URL configuration for tech_consulting project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, AppointmentViewSet

router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # Add other URLs as needed
]

# Example: Add a URL for a custom view
urlpatterns += [
    path('custom-view/', CustomView.as_view(), name='custom-view'),
]

# Example: Add a URL for the Django admin
from django.contrib import admin
urlpatterns += [
    path('admin/', admin.site.urls),
]

# Add authentication URLs if using TokenAuthentication
from rest_framework.authtoken import views as auth_views
urlpatterns += [
    path('api-token-auth/', auth_views.obtain_auth_token, name='api_token_auth'),
]

