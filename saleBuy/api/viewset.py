from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from saleBuy.models import SaleBuy
from saleBuy.api.serializers import SaleBuySerializers



class SaleBuyViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SaleBuy.objects.all()
    serializer_class = SaleBuySerializers
   # permission_classes = [permissions.IsAuthenticated]
