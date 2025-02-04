from django.urls import path
from forumuser import views as user_views

urlpatterns = [
    path('about/', user_views.about, name='about'),
    path('profile/update/', user_views.profile_update, name='profile_update'),
    path('', user_views.profile, name='profile'),
]
