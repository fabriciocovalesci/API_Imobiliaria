from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from address.models import Address

class AddressSerializer(ModelSerializer):

    class Meta:
        model = Address
        fields = ('id', 'state', 'city', 'neighborhood', 'street', 'number', 'cep')


