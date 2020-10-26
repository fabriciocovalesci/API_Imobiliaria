from django.contrib.auth.models import User, Group
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from immobile.models import Immobile, TypeImmobile
from immobile.api.serializers import ImmobileSerializer, TypeSerializers

class TypeViewSet(ModelViewSet):
    queryset = TypeImmobile.objects.all()
    serializer_class = TypeSerializers

class ImmobileViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Immobile.objects.all()
    serializer_class = ImmobileSerializer
