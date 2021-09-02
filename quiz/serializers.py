from rest_framework import serializers

from .models import Quiz, Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'text')


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id', 'text', 'type', 'answers')


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id', 'title')


class QuizDetailSerializer(QuizSerializer):
    questions = QuestionSerializer(many=True)

    class Meta(QuizSerializer.Meta):
        fields = QuizSerializer.Meta.fields + (
            'description', 'start_date', 'end_date', 'questions')
