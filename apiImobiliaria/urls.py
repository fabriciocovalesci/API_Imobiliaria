from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers


from compraVenda.api.viewset import UsuarioViewSet
from immobile.api.viewset import ImmobileViewSet, TypeViewSet
from address.api.viewSet import AddressViewSet
from accounts.views import ProfileViewSet
from accounts.views import RegisterAPI, LoginAPI, ShowUsers, ProfileViewSet


router = routers.DefaultRouter()
router.register(r'api/v1/usuario', ProfileViewSet)
router.register(r'api/v1/address', AddressViewSet)
router.register(r'api/v1/immobiletype', TypeViewSet)
router.register(r'api/v1/immobile', ImmobileViewSet)
router.register(r'api/v1/address', AddressViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('accounts.urls')),
    path('', include(router.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


