from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="forum_question")
    title = models.CharField(max_length=200, unique=True)
    detail = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | Asked by {self.user}"


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='forum_answers')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    detail = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Answer {self.detail} by {self.user}"
