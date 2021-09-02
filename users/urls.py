from django.urls import path, include
from rest_framework import routers

from .views import UserModelViewSet


router = routers.DefaultRouter()
router.register('users', UserModelViewSet)


urlpatterns = [
    path('', include(router.urls)),
]