from rest_framework import serializers
from immobile.models import Immobile, TypeImmobile


class TypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = TypeImmobile
        fields = ('id', 'typeIm')

class ImmobileSerializer(serializers.ModelSerializer):

    typeIm = TypeSerializers()
    
    class Meta:
        model = Immobile
        fields = ('id', 'title', 'description', 'condominium', 'typeIm', 'photo' )

