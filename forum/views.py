from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Question, Answer
from .forms import AnswerForm, QuestionForm


# Question List
def home(request):
    """
    Display all questions in the forum with pagination and search
    **context**
    questions: all questions in the forum
    **template**
    forum/question_list.html
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
    Display a single question and its answers with pagination and form
    **context**
    question: the question to be displayed
    answers: all answers to the question
    answer_form: form to submit an answer
    **template**
    forum/question_detail.html
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


# update answer
@login_required
def update_answer(request, answer_id):
    """
    Update an answer by the user who posted it and
    redirect to the question detail page
    **context**
    answer: the answer to be updated
    form: form to update the answer
    **template**
    forum/answer_form.html
    """
    answer = get_object_or_404(Answer, pk=answer_id, user=request.user)
    if request.method == 'POST':
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            form.save()
            return redirect('question_detail', question_id=answer.question.id)
    else:
        form = AnswerForm(instance=answer)
    return render(request, 'forum/answer_form.html', {'form': form})


# Ask Question
@login_required
def ask_question(request):
    """
    Allow users to ask questions and redirect to the home page
    **context**
    form: form to ask a question
    **template**
    forum/ask_question.html
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            form.save()
            messages.success(request, 'Your question has been posted.')
            return redirect('home')
    else:
        form = QuestionForm()
    return render(request, 'forum/ask_question.html', {'form': form})


# update question
@login_required
def update_question(request, question_id):
    """
    Update a question by the user who posted it and
    redirect to the question detail page
    **context**
    question: the question to be updated
    form: form to update the question
    **template**
    forum/question_form.html
    """
    question = get_object_or_404(Question, pk=question_id, user=request.user)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('question_detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    return render(request, 'forum/update_question.html', {'form': form})


# delete question
@login_required
def delete_question(request, question_id):
    """
    Delete a question by the user who posted it and
    redirect to the home page
    **context**
    question: the question to be deleted
    **template**
    forum/confirm_delete.html
    """
    question = get_object_or_404(Question, pk=question_id, user=request.user)
    if request.method == 'POST':
        question.delete()
        messages.success(request, 'Your question has been deleted.')
        return redirect('home')
    return render(
        request, 'forum/confirm_delete.html', {'question': question})


# delete answer
@login_required
def delete_answer(request, answer_id):
    """
    Delete an answer by the user who posted it and
    redirect to the question detail page
    **context**
    answer: the answer to be deleted
    **template**
    forum/confirm_delete_answer.html
    """
    answer = get_object_or_404(Answer, pk=answer_id, user=request.user)
    if request.method == 'POST':
        answer.delete()
        return redirect('question_detail', question_id=answer.question.id)
    return render(
        request, 'forum/confirm_delete_answer.html', {'answer': answer})


# custom 404
def custom_404(request, exception):
    return render(request, 'buratiforum/templates/404.html', status=404)


# custom 400
def custom_400(request, exception):
    return render(request, 'buratiforum/templates/400.html', status=400)


# custom 500
def custom_500(request):
    return render(request, 'buratiforum/templates/500.html', status=500)


# custom 403
def custom_403(request, exception):
    return render(request, 'buratiforum/templates/403.html', status=403)
