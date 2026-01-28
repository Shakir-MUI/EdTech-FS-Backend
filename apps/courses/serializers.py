from rest_framework import serializers
from .models import Topic, Lesson
from apps.quizzes.serializers import QuizSerializer
from django.conf import settings

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ["id", "title", "order"]


class LessonDetailSerializer(serializers.ModelSerializer):
    topic = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = ["id", "title", "content", "order", "topic"]

    def get_topic(self, obj):
        lessons = obj.topic.lessons.values("id", "title", "order")
        return {
            "title": obj.topic.title,
            "slug": obj.topic.slug,
            "lessons": sorted(lessons, key=lambda x: x["order"])
        }


class TopicSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField() 
    lessons = LessonSerializer(many=True, read_only=True)
    quiz = QuizSerializer(read_only=True)  # One-to-One
    quizzes = serializers.SerializerMethodField()  # ← ARRAY for frontend

    class Meta:
        model = Topic
        fields = [
            "id",
            "title",
            "slug",
            "description",
            "image",
            "created_at",
            "lessons",
            "quiz",
            "quizzes",   # <-- frontend expects this
        ]

    def get_image(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(
            settings.STATIC_URL + obj.image
        )

    def get_quizzes(self, obj):
        """Frontend expects quizzes[] even though quiz is OneToOne."""
        if hasattr(obj, "quiz") and obj.quiz is not None:
            return [QuizSerializer(obj.quiz).data]
        return []
