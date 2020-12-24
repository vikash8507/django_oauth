from django.contrib.auth.models import User
from django import forms
from .models import Profile, Post


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('mobile', 'about', 'photo')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'