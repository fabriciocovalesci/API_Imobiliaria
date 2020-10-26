from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from address.models import Address
from address.api.serializers import AddressSerializer 


class AddressViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
