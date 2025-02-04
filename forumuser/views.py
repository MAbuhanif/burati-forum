from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import UserForm, ProfileForm


# Profile view
@login_required
def profile(request):
    """"
    Display the user's profile with the user form and profile form
    **Arguments**
    request: HttpRequest object
    **Returns**
    render: render the profile.html template with the user form,
    profile form and profile
    """
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)

    return render(request, 'forumuser/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'profile': profile
    })


@login_required
def profile_update(request):
    """
    Update the user's profile with the user form and profile form
    **Arguments**
    request: HttpRequest object
    **Returns**
    render: render the profile_update.html template with the user form,
    profile form and profile
    """
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)
    return render(request, 'forumuser/profile_update.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'profile': profile
    })


# About view
def about(request):
    """
    Display the about page with the about.html template
    """
    return render(request, 'forumuser/about.html')
