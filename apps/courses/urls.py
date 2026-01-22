from rest_framework import routers
from .views import TopicViewSet, LessonViewSet

router = routers.DefaultRouter()
router.register(r"topics", TopicViewSet, basename="topic")
router.register(r"lessons", LessonViewSet, basename="lesson")

urlpatterns = router.urls
