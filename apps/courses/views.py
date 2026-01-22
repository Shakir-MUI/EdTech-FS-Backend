from rest_framework import viewsets, permissions
from .models import Topic, Lesson
from .serializers import TopicSerializer, LessonSerializer, LessonDetailSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "slug"


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        # List → basic fields
        if self.action == "list":
            return LessonSerializer

        # GET /lessons/<id>/ → detailed fields
        return LessonDetailSerializer
