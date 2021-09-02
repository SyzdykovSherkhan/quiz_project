from django.urls import path, include
from rest_framework import routers

from .views import QuizViewSet, UserQuizResultViewSet


router = routers.DefaultRouter()
router.register('quizzes', QuizViewSet)
router.register('answers', UserQuizResultViewSet)


urlpatterns = [
    path('', include(router.urls)),
]