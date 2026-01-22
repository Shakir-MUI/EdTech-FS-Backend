from django.db import models


class Topic(models.Model):
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="subtopics",
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    # ✅ ADD THIS FIELD
    image = models.ImageField(upload_to="topics/", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    topic = models.ForeignKey(Topic, related_name="lessons", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)  # HTML / markdown allowed
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.topic.title} — {self.title}"
