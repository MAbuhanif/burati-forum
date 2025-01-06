from django import forms
from .models import Answer, Question


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('detail',)



class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'slug', 'description']