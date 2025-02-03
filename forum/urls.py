from django.urls import path
from . import views


urlpatterns = [
    path('ask/', views.ask_question, name='ask_question'), 
    path('question/<int:question_id>/', views.question_detail, name='question_detail'),
    path('question/<int:question_id>/edit/', views.update_question, name='update_question'),
    path('question/<int:question_id>/delete/', views.delete_question, name='delete_question'),
    path('answer/<int:answer_id>/delete/', views.delete_answer, name='delete_answer'),
    path('', views.home, name='home'),
]
handler404 = 'forum.views.custom_404'
