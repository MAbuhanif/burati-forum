from django.db import models
from django.contrib.auth.models import User

""""
    Question model
    This model represents the question that the user asks in the forum.
    user: This field is a ForeignKey to the User model. It represents the user who asked the question.
"""


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="forum_question")
    title = models.CharField(max_length=200, unique=True)
    detail = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)  

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | Asked by {self.user}"


"""
    Answer model
    This model represents the answer that the user gives to a question.
    question: This field is a ForeignKey to the Question model. It represents the question to which the user is answering.
"""


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    detail = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Answer {self.detail} by {self.user}"
