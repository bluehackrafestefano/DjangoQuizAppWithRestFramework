from django.contrib import admin
from .models import Question, Quiz, Answer, Category
import nested_admin

class AnswerInline(nested_admin.NestedStackedInline):
    model = Answer
    extra = 4
    max_num = 8

class QuestionInline(nested_admin.NestedStackedInline):
    model = Question
    extra = 5  # how many to see on the page
    max_num = 8  # limit of questions on the page
    inlines = [AnswerInline]

class QuizAdmin(nested_admin.NestedModelAdmin):
    inlines = [QuestionInline]


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Category)
