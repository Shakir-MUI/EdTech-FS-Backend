from django.contrib import admin
from .models import Topic, Lesson

class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 0

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug", "created_at")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [LessonInline]

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "topic", "order")
    list_filter = ("topic",)
    ordering = ("topic", "order")
