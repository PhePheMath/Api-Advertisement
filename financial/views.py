from django.shortcuts import render
from rest_framework import viewsets

from . import models, serializers

class PromotionViewSet(viewsets.ModelViewSet):
    queryset = models.Promotion.objects.all()
    serializer_class = serializers.PromotionSerializer


class PostsViewSet(viewsets.ModelViewSet):
    queryset = models.Posts.objects.all()
    serializer_class = serializers.PostsSerializer
