from django.utils import timezone
from django.contrib.auth import get_user_model
from rest_framework import viewsets, mixins

from .models import Quiz, UserQuizResult
from .serializers import QuizSerializer, QuizDetailSerializer, \
    UserQuizResultSerializer, UserQuizResultDetailSerializer

UserModel = get_user_model()


class QuizViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    detail_serializer_class = QuizDetailSerializer

    def get_queryset(self):
        return self.queryset.filter(start_date__lte=timezone.now(),
                                    end_date__gte=timezone.now())


class UserQuizResultViewSet(viewsets.ModelViewSet):
    queryset = UserQuizResult.objects.all()
    serializer_class = UserQuizResultDetailSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            self.serializer_class = UserQuizResultSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        if isinstance(self.request.user, UserModel):
            serializer.save(user_id=self.request.user.id)
        else:
            serializer.save(user_id=self.request.COOKIES['user_id'])
        super().perform_create(serializer)
