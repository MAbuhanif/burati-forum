from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserForm(forms.ModelForm):
    """
    UserForm class to create a form for the User model.
    """
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileForm(forms.ModelForm):
    """
    ProfileForm class to create a form for the Profile model.
    """
    class Meta:
        model = Profile
        fields = ['bio', 'phone', 'profile_image']
