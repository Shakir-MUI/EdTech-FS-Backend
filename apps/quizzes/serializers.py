from rest_framework import serializers
from .models import Quiz, Question, UserQuizResult


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        exclude = ["correct_option", "quiz"]


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ["id", "title", "total_marks", "questions"]


class SubmitQuizSerializer(serializers.Serializer):
    answers = serializers.DictField(child=serializers.CharField())


class UserQuizResultSerializer(serializers.ModelSerializer):
    quiz = serializers.CharField(source="quiz.title", read_only=True)

    class Meta:
        model = UserQuizResult
        fields = ["quiz", "score", "taken_at"]
