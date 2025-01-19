from . import views
from django.urls import path
from .views import question_list, ask_question


urlpatterns = [
    path('ask/', ask_question, name='ask_question'), 
    path('<int:id>/', views.question_detail, name='question_detail'),
    path('', question_list, name='question_list'),
]