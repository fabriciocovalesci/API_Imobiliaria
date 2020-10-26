"""apiImobiliaria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from compraVenda.api.viewset import UsuarioViewSet
from immobile.api.viewset import ImmobileViewSet, TypeViewSet
from address.api.viewSet import AddressViewSet
from accounts.views import ProfileViewSet


router = routers.DefaultRouter()
router.register(r'api/v1/usuario', ProfileViewSet)
router.register(r'api/v1/address', AddressViewSet)
router.register(r'api/v1/immobiletype', TypeViewSet)
router.register(r'api/v1/immobile', ImmobileViewSet)
router.register(r'api/v1/address', AddressViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include(router.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


