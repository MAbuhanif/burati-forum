from . import views
from django.urls import path
from .views import question_list, ask_question
from forumuser import views as user_views



urlpatterns = [
    path('ask/', ask_question, name='ask_question'), 
    path('<slug:slug>/', views.question_detail, name='question_detail'),
    path('', question_list, name='question_list'),
]