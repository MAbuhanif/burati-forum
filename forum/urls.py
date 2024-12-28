from . import views
from django.urls import path


urlpatterns = [
    path('', views.QuestionList.as_view(), name='home'),
    path('<slug:slug>/', views.question_detail, name='question_detail'),
]