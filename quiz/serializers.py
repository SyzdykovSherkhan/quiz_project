from rest_framework import serializers

from .models import Quiz, Question, Answer, UserQuizResult, UserAnswer


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


class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = ('question', 'text', 'answers_ids')


class UserQuizResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserQuizResult
        fields = ('id', 'quiz')


class UserQuizResultDetailSerializer(UserQuizResultSerializer):
    user_answers = UserAnswerSerializer(many=True)

    class Meta(UserQuizResultSerializer.Meta):
        fields = UserQuizResultSerializer.Meta.fields + ('user_answers', )

    def create(self, validated_data):
        user_answers = validated_data.pop('user_answers')
        user_quiz_result = super().create(validated_data)
        if user_answers:
            for user_answer in user_answers:
                UserAnswer.objects.create(**user_answer,
                                          user_quiz_result=user_quiz_result)
        return user_quiz_result

    def update(self, instance, validated_data):
        validated_data.pop('user_answers')
        return super().update(instance, validated_data)
