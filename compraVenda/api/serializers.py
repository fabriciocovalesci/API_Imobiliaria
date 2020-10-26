from rest_framework import serializers
from compraVenda.models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = ('id', 'first_name', 'last_name','email', 'account', 'telefone')
