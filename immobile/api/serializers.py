from rest_framework import serializers
from drf_writable_nested import UniqueFieldsMixin , WritableNestedModelSerializer

from immobile.models import Immobile, TypeImmobile
from address.api.serializers import AddressStreetSerializer


class TypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = TypeImmobile
        fields = ('id', 'typeIm')

class ImmobileSerializer(WritableNestedModelSerializer):

    class Meta:
        depth = 1
        fields = ['id', 'title', 'description', 'amount', 'condominium', 'typeIm', 'photo', 'address' ]
        model = Immobile
    
    typeIm = TypeSerializers()
    address = AddressStreetSerializer()

   