from rest_framework import serializers
from .models import Advertiser, Personnel, User

class AdvertiserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Advertiser
        fields = ['id', 'user']


class PersonnelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Personnel
        fields = ['user', 'enterprise', 'authority']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
