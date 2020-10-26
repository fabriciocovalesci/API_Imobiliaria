from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from compraVenda.models import Usuario
from compraVenda.api.serializers import UsuarioSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
