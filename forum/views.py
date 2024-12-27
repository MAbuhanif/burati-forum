from django.shortcuts import render
from django.views import generic
from .models import Question


# Create your views here.
class QuestionList(generic.ListView):
    queryset = Question.objects.all()
    template_name = "forum/index.html"
    paginate_by = 6
