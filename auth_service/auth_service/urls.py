"""
URL configuration for auth_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


# Swagger configuration
schema_view = get_schema_view(
    openapi.Info(
        title="Auth Service API",
        default_version="v1",
        description="This is the API documentation for Grammar AZI.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@myapi.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Admin panel
    path(
        "admin/", 
        admin.site.urls
    ),

    # Swagger and ReDoc documentation
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="swagger-ui",
    ),
    
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="redoc-ui",
    ),

    # Endpoints for JWT authentication
    path(
        "api/token/", 
        TokenObtainPairView.as_view(),
        name="token_obtain_pair"
    ),

    path(
        "api/token/refresh/", 
        TokenRefreshView.as_view(), 
        name="token_refresh"
    ),

    path(
        "api/token/verify/", 
        TokenVerifyView.as_view(), 
        name="token_verify"
    ),
    
    # API paths
    path(
        "api/v1/", 
        include("users.urls")
    ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)