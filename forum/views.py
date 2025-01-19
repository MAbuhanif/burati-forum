from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Question
from .forms import AnswerForm, QuestionForm


def question_list(request):
    """
    search for questions by title
    """
    query = request.GET.get('q')
    if query:
        questions = Question.objects.filter(title__icontains=query).order_by('-created_on')
    else:
        questions = Question.objects.all().order_by('-created_on')
    paginator = Paginator(questions, 4)
    page_number = request.GET.get('page')
    questions = paginator.get_page(page_number)
    return render(request, 'forum/question_list.html', {'questions': questions, })

# Ask Question


def ask_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('question_list')
    else:
        form = QuestionForm()
    return render(request, 'forum/ask_question.html', {'form': form})


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
    question = get_object_or_404(queryset, id=id)
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
