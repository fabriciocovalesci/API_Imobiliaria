from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from lease.models import Lease
from address.models import  AddressStreet
from accounts.serializers import ProfileSerializer
from immobile.api.serializers import ImmobileSerializer 


class LeaseSerializers(WritableNestedModelSerializer):

    client = ProfileSerializer()

    salesman = ProfileSerializer()

    immobile = ImmobileSerializer()

    class Meta:
        model = Lease
        fields = ['id', 'amount', 'date', 'client', 'salesman', 'immobile', 'multa', 'payday']

