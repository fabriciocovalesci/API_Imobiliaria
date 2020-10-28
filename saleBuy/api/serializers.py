from saleBuy.models import SaleBuy
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from address.models import  AddressStreet
from accounts.serializers import ProfileSerializer
from immobile.api.serializers import ImmobileSerializer 

from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

class SaleBuySerializers(ModelSerializer):

    client = ProfileSerializer()

    salesman = ProfileSerializer()

    immobile = ImmobileSerializer()

    class Meta:
        model = SaleBuy
        fields = ['id', 'amount', 'date', 'client', 'salesman', 'immobile']
