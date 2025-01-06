from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Question
from .forms import AnswerForm, QuestionForm


# Create your views here.
# class QuestionList(generic.ListView):
#     queryset = Question.objects.all()
#     template_name = "forum/index.html"
#     paginate_by = 4

def question_list(request):
    query = request.GET.get('q')
    if query:
        questions = Question.objects.filter(title__icontains=query).order_by('-created_on')
    else:
        questions = Question.objects.all().order_by('-created_on')
    questions = Question.objects.all().order_by('-created_on')  # Adjust query as needed
    paginator = Paginator(questions, 4)  # Show 4 questions per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'forum/question_list.html', {'page_obj': page_obj, 'query': query})

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
