from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import Profile
from address.api.serializers import AddressSerializer
from address.models import Address

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user


class ShowUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class ProfileSerializer(serializers.ModelSerializer):

    address = AddressSerializer()
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ('id',  'cpf', 'account', 'cellphone', 'address', 'user')


    def create(self, validated_data):
        addres = Address.objects.get(pk=validated_data.pop('address_id')).get('id')
        instance = Profile.objects.create(**validated_data)
        User.objects.create(Address=addres, Profile=instance)
        return instance

    # def to_representation(self, instance):
    #     representation = super(EquipmentSerializer, self).to_representation(instance)
    #     representation['assigment'] = AssignmentSerializer(instance.assigment_set.all(), many=True).data
    #     return representation














# class UserProfileSerializer(serializers.ModelSerializer):
#     """A serializer for our user profile objects."""

#     class Meta:
#         model = models.UserProfile
#         fields = ('id', 'email', 'name', 'password')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         """Create and return a new user."""

#         user = models.UserProfile(
#             email=validated_data['email'],
#             name=validated_data['name']
#         )

#         user.set_password(validated_data['password'])
#         user.save()

#         return user