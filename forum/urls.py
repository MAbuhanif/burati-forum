from django.urls import path
from . import views


urlpatterns = [
    path('ask/', views.ask_question, name='ask_question'), 
    path('question/<int:question_id>/', views.question_detail, name='question_detail'),
    path('question/<int:question_id>/edit/', views.update_question, name='update_question'),
    path('question/<int:question_id>/delete/', views.delete_question, name='delete_question'),
    path('answer/<int:answer_id>/delete/', views.delete_answer, name='delete_answer'),
    path('', views.question_list, name='question_list'),
]
handler404 = 'forumuser.views.custom_404'