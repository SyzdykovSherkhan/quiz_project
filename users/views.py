from rest_framework import viewsets, mixins
from .models import UserModel
from .serializers import UserModelSerializer


class UserModelViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin,
                       viewsets.GenericViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
