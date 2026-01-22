from django.contrib import admin
from .models import Quiz, Question, UserQuizResult


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 2
    fields = ("text", "option_a", "option_b", "option_c", "option_d", "correct_option", "marks")


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ("title", "topic", "total_marks")
    list_filter = ("topic",)
    search_fields = ("title",)
    inlines = [QuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "quiz", "correct_option", "marks")
    list_filter = ("quiz",)
    search_fields = ("text",)


@admin.register(UserQuizResult)
class UserQuizResultAdmin(admin.ModelAdmin):
    list_display = ("user", "quiz", "score", "taken_at")
    list_filter = ("quiz", "taken_at")
    search_fields = ("user__username", "quiz__title")
    readonly_fields = ("score", "taken_at")
