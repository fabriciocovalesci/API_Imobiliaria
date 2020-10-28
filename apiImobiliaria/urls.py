from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers


from immobile.api.viewset import ImmobileViewSet, TypeViewSet
from address.api.viewSet import AddressViewSet
from accounts.views import RegisterAPI, LoginAPI, ShowUsers, ProfileViewSet
from saleBuy.api.viewset import SaleBuyViewSet
from lease.api.viewset import LeaseViewSet


router = routers.DefaultRouter()
router.register(r'api/v1/profile', ProfileViewSet)
router.register(r'api/v1/address', AddressViewSet)
router.register(r'api/v1/immobiletype', TypeViewSet)
router.register(r'api/v1/immobile', ImmobileViewSet)
router.register(r'api/v1/saleBuy', SaleBuyViewSet)
router.register(r'api/v1/lease', LeaseViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include(router.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


