from rest_framework import serializers
from drf_writable_nested import UniqueFieldsMixin , WritableNestedModelSerializer

from immobile.models import Immobile, TypeImmobile


class TypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = TypeImmobile
        fields = ('id', 'typeIm')

class ImmobileSerializer(UniqueFieldsMixin, WritableNestedModelSerializer):

    
    class Meta:
        depth = 1
        fields = ['id', 'title', 'description', 'condominium', 'typeIm', 'photo', ]
        model = Immobile
    
    typeIm = TypeSerializers()

   