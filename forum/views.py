from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Question, Answer
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


@login_required
def question_detail(request, pk):
    """
    Display question and answers  
    """
    queryset = Question.objects.all()
    question = get_object_or_404(queryset, pk=pk)
    answers = Answer.objects.filter(question=question)
    answer_form = AnswerForm()

    if request.method == "POST":
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            answer = answer_form.save(commit=False)
            answer.question = question
            answer.user = request.user
            answer.save()  
            messages.success(request, "Your answer has been submitted for review")
            return redirect("question_detail", pk=question.pk)
    else:
        answer_form = AnswerForm()                     
    return render(
        request,
        "forum/question_detail.html",
        {
            "question": question,
            "answer_form" : answer_form,
            "answers": answers,
        },
    )
