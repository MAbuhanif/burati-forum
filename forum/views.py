from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Question
from .forms import AnswerForm


# Create your views here.
class QuestionList(generic.ListView):
    queryset = Question.objects.all()
    template_name = "forum/index.html"
    paginate_by = 6



def question_detail(request, slug):
    """
    Display an individual :model:`question.Post`.

    **Context**

    ``question``
        An instance of :model:`forum.Question`.

    **Template:**

    :template:`forum/question_detail.html`
    """

    queryset = Question.objects.all()
    question = get_object_or_404(queryset, slug=slug)
    answers = question.answers.all().order_by("-created_on")
    answer_count = question.answers.filter(approved=True).count()
    answer_form =AnswerForm()

    return render(
        request,
        "forum/question_detail.html",
        {
            "question": question,
            "answers" : answers,
            "answer_count" : answer_count,
            "answer_form" : answer_form,
        },
    )
