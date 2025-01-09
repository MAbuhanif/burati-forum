from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile


# Create your views here.
def profile(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    return render(request, 'forumuser/profile.html', {'profile': profile})
