from django import forms
from .models import Answer, Question


class QuestionForm(forms.ModelForm):
    """
    QuestionForm class to create a form for the Question model.
    """
    class Meta:
        model = Question
        fields = ['title', 'detail', ]


class AnswerForm(forms.ModelForm):
    """
    AnswerForm class to create a form for the Answer model.
    """
    class Meta:
        model = Answer
        fields = ('detail',)
