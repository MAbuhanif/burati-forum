from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Question, Answer
from .forms import AnswerForm, QuestionForm


# Question List
def question_list(request):
    """
    search for questions by title
    """
    query = request.GET.get('q')
    if query:
        questions = Question.objects.filter(title__icontains=query).order_by(
            '-created_on')
    else:
        questions = Question.objects.all().order_by('-created_on')
    paginator = Paginator(questions, 4)
    page_number = request.GET.get('page')
    questions = paginator.get_page(page_number)
    return render(
        request, 'forum/question_list.html', {'questions': questions, })


# Question Detail
def question_detail(request, question_id):
    """
    Display question and answers
    """
    queryset = Question.objects.all()
    question = get_object_or_404(queryset, pk=question_id)
    answers = Answer.objects.filter(question=question)
    answer_form = AnswerForm()

    if request.method == "POST":
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            answer = answer_form.save(commit=False)
            answer.question = question
            answer.user = request.user
            answer.save()
            messages.success(
                request,
                "Your answer has been submitted for review"
            )
            return redirect("question_detail", question_id=question.id)
    else:
        answer_form = AnswerForm()
    return render(
        request,
        "forum/question_detail.html",
        {
            "question": question,
            "answer_form": answer_form,
            "answers": answers,
        },
    )


# Ask Question
@login_required
def ask_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            form.save()
            messages.success(request, 'Your question has been posted.')
            return redirect('question_list')
    else:
        form = QuestionForm()
    return render(request, 'forum/ask_question.html', {'form': form})


# update question
@login_required
def update_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id, user=request.user)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('question_detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    return render(request, 'forum/question_form.html', {'form': form})


@login_required
def delete_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id, user=request.user)
    if request.method == 'POST':
        question.delete()
        return redirect('question_list')
    return render(request, 'forum/confirm_delete.html', {'question': question})


@login_required
def delete_answer(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id, user=request.user)
    if request.method == 'POST':
        answer.delete()
        return redirect('question_detail', question_id=answer.question.id)
    return render(
        request, 'forum/confirm_delete_answer.html', {'answer': answer})
