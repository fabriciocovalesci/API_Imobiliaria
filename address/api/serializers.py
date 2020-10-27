from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from address.models import  AddresState, AddressCity, AddressNeighborhood, AddressStreet
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

class AddressStateSerializer(ModelSerializer):
    class Meta:
        model = AddresState
        fields = ('id', 'state',)

class AddressCitySerializer(ModelSerializer):
    class Meta:
        model = AddressCity
        fields = ('id', 'city', )


class AddressNeighborhoodSerializer(ModelSerializer):
    class Meta:
        model = AddressNeighborhood
        fields = ('id', 'neighborhood',)


class AddressStreetSerializer(WritableNestedModelSerializer):

    state = AddressStateSerializer()

    city = AddressCitySerializer()
    
    neighborhood = AddressNeighborhoodSerializer()

    class Meta:
        model = AddressStreet
        fields = ('id', 'state', 'city', 'neighborhood', 'street', 'number', 'cep',)




