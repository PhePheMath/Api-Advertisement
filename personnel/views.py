from django.shortcuts import render
from rest_framework import viewsets

from . import models, serializers

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class AdvertiserViewSet(viewsets.ModelViewSet):
    queryset = models.Advertiser.objects.all()
    serializer_class = serializers.AdvertiserSerializer


class PersonnelViewSet(viewsets.ModelViewSet):
    queryset = models.Personnel.objects.all()
    serializer_class = serializers.PersonnelSerializer
