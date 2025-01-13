from django.shortcuts import render
from .models import Profile


# Create your views here.
def profile(request):
    profile = Profile.objects.all().order_by('user').first()
    return render(request, 'forumuser/profile.html', {'profile': profile})
