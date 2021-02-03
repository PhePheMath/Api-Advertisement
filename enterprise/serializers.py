from rest_framework import serializers
from .models import Enterprise, Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'enterprise']


class EnterpriseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Enterprise
        fields = ['name']
