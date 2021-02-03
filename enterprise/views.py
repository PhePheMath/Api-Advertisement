from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from rest_framework import viewsets

from . import models, serializers

class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def post(self, request, *args, **kwargs):
        user = request.user

        try:
            has_authority = user.as_personnel.authority == 1
            has_permission = user.has_perm('enterprise.product')
            if has_authority or has_permission:
                return super(ProductViewSet, self).post(request, *args, **kwargs)
            else:
                return PermissionDenied('You dont have permission')
        except user.RelatedObjectDoesNotExist:
            return PermissionDenied

    def destroy(self, request, *args, **kwargs):
        user = request.user

        try:
            has_authority = user.as_personnel.authority == 1
            has_permission = user.has_perm('enterprise.product')
            is_related = self.get_object().enterprise.workers.get(pk=self.request.user.pk)
            if (has_authority or has_permission) and is_related:
                return super(ProductViewSet, self).destroy(request, *args, **kwargs)
            else:
                return PermissionDenied('Your authority isn\'t enough!')
        except user.RelatedObjectDoesNotExist:
            return PermissionDenied

class EnterpriseViewSet(viewsets.ModelViewSet):
    queryset = models.Enterprise.objects.all()
    serializer_class = serializers.EnterpriseSerializer

    def destroy(self, request, *args, **kwargs):
        user = request.user

        try:
            has_authority = user.as_personnel.authority > 3
            if has_authority:
                return super(EnterpriseViewSet, self).destroy(request, *args, **kwargs)
            else:                
                return PermissionDenied('Your authority isn\'t enough!')
        except user.RelatedObjectDoesNotExist:
            return PermissionDenied
