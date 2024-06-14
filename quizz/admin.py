from django.contrib import admin
from .models import Quiz, Question

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

admin.site.register(Quiz, QuizAdmin)
