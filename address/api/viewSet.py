from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from address.models import AddressStreet
from address.api.serializers import AddressStreetSerializer 

class AddressViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AddressStreet.objects.all()
    serializer_class = AddressStreetSerializer
    #permission_classes = [permissions.IsAuthenticated]
