from rest_framework import serializers
from .models import Promotion, Posts

class PromotionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Promotion
        fields = ['product', 'value', 'goal', 'ignore_negative']


class PostsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posts
        fields = ['promotion', 'advertiser']
