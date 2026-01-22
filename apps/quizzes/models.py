from django.db import models
from apps.courses.models import Topic
from django.contrib.auth.models import User


class Quiz(models.Model):
    topic = models.OneToOneField(
        Topic,
        on_delete=models.CASCADE,
        related_name="quiz"
    )
    title = models.CharField(max_length=255)
    total_marks = models.IntegerField(default=15)

    def __str__(self):
        return f"{self.topic.title} Quiz"


class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name="questions"
    )
    text = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=1)
    marks = models.IntegerField(default=1)

    def __str__(self):
        return self.text[:80]



class UserQuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()
    taken_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-taken_at"]

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title}: {self.score}"
