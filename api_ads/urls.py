"""api_ads URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from financial.views import PromotionViewSet, PostsViewSet
from enterprise.views import EnterpriseViewSet, ProductViewSet
from personnel.views import UserViewSet, AdvertiserViewSet, PersonnelViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from rest_framework import routers

router = routers.DefaultRouter()
router.register('promotion', PromotionViewSet)
router.register('posts', PostsViewSet)
router.register('enterprise', EnterpriseViewSet)
router.register('product', ProductViewSet, 'product')
router.register('user', UserViewSet)
router.register('advertiser', AdvertiserViewSet)
router.register('personnel', PersonnelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
