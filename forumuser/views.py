from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile



@login_required
def profile(request):
    profile = Profile.objects.all().order_by('user').first()
    return render(request, 'forumuser/profile.html', {'profile': profile})
