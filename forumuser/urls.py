from django.urls import path
from forumuser import views as user_views

urlpatterns = [
    path('', user_views.profile, name='profile'),
]