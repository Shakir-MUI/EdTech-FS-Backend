from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .models import Quiz, UserQuizResult
from apps.courses.models import Topic
from .serializers import QuizSerializer, SubmitQuizSerializer


class TopicQuizView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, slug):
        topic = Topic.objects.get(slug=slug)
        quiz = topic.quiz
        serializer = QuizSerializer(quiz)
        return Response(serializer.data)
    

class SubmitTopicQuizView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, slug):
        topic = Topic.objects.get(slug=slug)
        quiz = topic.quiz

        serializer = SubmitQuizSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        answers = serializer.validated_data["answers"]
        total = quiz.total_marks
        correct = 0

        for q in quiz.questions.all():
            if answers.get(str(q.id)) == q.correct_option:
                correct += 1

        UserQuizResult.objects.create(
            user=request.user,
            quiz=quiz,
            score=correct
        )

        return Response({
            "score": correct,
            "out_of": total
        })
