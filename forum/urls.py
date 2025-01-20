from django.urls import path
from . import views


urlpatterns = [
    path('ask/', views.ask_question, name='ask_question'), 
    path('<int:pk>/', views.question_detail, name='question_detail'),
    path('', views.question_list, name='question_list'),
]