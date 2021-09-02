from django.db import models
from django.contrib.postgres.fields import ArrayField


class Quiz(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}: quiz'


class Question(models.Model):
    class Types(models.IntegerChoices):
        SINGLE_ANSWER = 0, 'SINGLE_ANSWER'
        MULTIPLE_ANSWERS = 1, 'MULTIPLE_ANSWERS'
        TEXT_ANSWER = 2, 'ANSWER_WITH_TEXT'

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE,
                             related_name='questions')

    text = models.TextField()
    type = models.IntegerField(choices=Types.choices,
                               default=Types.SINGLE_ANSWER)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Answer(models.Model):
    question = models.ManyToManyField(Question, related_name='answers')
    text = models.TextField()
    score = models.PositiveSmallIntegerField(null=True, blank=True)


class UserQuizResult(models.Model):
    user_id = models.PositiveBigIntegerField()
    quiz = models.ForeignKey(Quiz, on_delete=models.SET_NULL, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class UserAnswer(models.Model):
    user_quiz_result = models.ForeignKey(UserQuizResult,
                                         on_delete=models.CASCADE)
    question = models.OneToOneField(Question, on_delete=models.SET_NULL,
                                    null=True)
    text = models.TextField(null=True, blank=True)
    answers_ids = ArrayField(
        models.PositiveIntegerField(null=True, blank=True)
    )
