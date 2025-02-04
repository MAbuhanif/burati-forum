from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    """
    Model for the Question
    purpose of this model is to store the question asked by the user
    foreign key is used to link the question with the user :model:`auth.User`
    """
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
    """
    Model for the Answer
    purpose of this model is to store the answer given by the user
    foreign key is used to link the answer with the question
    """
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
