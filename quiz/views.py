from rest_framework import viewsets, mixins

from .models import Quiz
from .serializers import QuizSerializer, QuizDetailSerializer


class QuizViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return QuizDetailSerializer
        return super().get_serializer_class()
