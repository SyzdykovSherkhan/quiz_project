import nested_admin
from django.contrib import admin

from .models import Quiz, Question, Answer, UserQuizResult, UserAnswer


class AnswerAdmin(admin.ModelAdmin):
    ...


class QuestionAdmin(admin.ModelAdmin):
    ...


class QuestionInline(nested_admin.NestedTabularInline):
    model = Question
    fields = ('text', 'type')
    extra = 0


class QuizAdmin(nested_admin.NestedModelAdmin):
    inlines = (QuestionInline, )
    list_display = ('id', 'start_date', 'end_date')
    readonly_fields = ('created', 'modified')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        try:
            if not request.user.is_superuser:
                form.base_fields['start_date'].disabled = True
        except KeyError:
            ...
        return form


class UserAnswerAdmin(nested_admin.NestedTabularInline):
    model = UserAnswer
    fields = ('question', 'text', 'answers_ids')
    extra = 0

    def has_add_permission(self, request, *args, **kwargs):
        return False


class UserQuizResultAdmin(nested_admin.NestedModelAdmin):
    inlines = (UserAnswerAdmin, )
    list_display = ('id', 'user_id', 'quiz')
    readonly_fields = ('user_id', 'quiz', 'created', 'modified')

    def has_add_permission(self, request, *args, **kwargs):
        return False


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(UserQuizResult, UserQuizResultAdmin)

