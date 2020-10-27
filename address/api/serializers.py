from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from address.models import  AddresState, AddressCity, AddressNeighborhood, AddressStreet
from drf_writable_nested import UniqueFieldsMixin , WritableNestedModelSerializer

class AddressStateSerializer(ModelSerializer):

    class Meta:
        model = AddresState
        fields = ('id', 'state',)

class AddressCitySerializer(ModelSerializer):
    
    state = AddressStateSerializer()
    class Meta:
        model = AddressCity
        fields = ('id', 'state', 'city', )


class AddressNeighborhoodSerializer(ModelSerializer):

    city = AddressCitySerializer()
    class Meta:
        model = AddressNeighborhood
        fields = ('id', 'city', 'neighborhood',)


class AddressStreetSerializer(UniqueFieldsMixin, WritableNestedModelSerializer):

    state = AddressStateSerializer()

    city = AddressCitySerializer()

    neighborhood = AddressNeighborhoodSerializer()
    class Meta:
        model = AddressStreet()
        fields = ('id', 'state', 'city', 'neighborhood', 'street', 'number', 'cep',)




