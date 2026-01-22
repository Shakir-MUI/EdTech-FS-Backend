from django.urls import path
from .views import TopicQuizView, SubmitTopicQuizView

urlpatterns = [
    path("<slug:slug>/", TopicQuizView.as_view(), name="topic-quiz"),
    path("submit/<slug:slug>/", SubmitTopicQuizView.as_view(), name="submit-topic-quiz"),
]
