from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .models import Profile, Post
from .forms import UserEditForm, ProfileEditForm, PostForm


def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'django_app/home.html', context)


@login_required
def dashboard(request):
    user = request.user
    profile = Profile.objects.filter(user=user).first()
    context = {
        'profile': profile
    }
    return render(request, 'django_app/dashboard.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('dashboard')
        else:
            return redirect('edit_profile')
    else:
        user_form = UserEditForm(instance=request.user)
        try:
            profile_form = ProfileEditForm(instance=request.user.profile)
        except:
            profile = Profile(user=request.user)
            profile.save()
            profile_form = ProfileEditForm(instance=profile)
        context = {
            'profile_form': profile_form,
            'user_form': user_form
        }
        return render(request, 'django_app/edit_profile.html', context)


@login_required
def post(request):
    if request.method == 'POST':
        post = PostForm(request.POST, request.FILES)
        if post.is_valid():
            post.save()
            return redirect('home')
        else:
            return redirect('post')
    else:
        post = PostForm()
        return render(request, 'django_app/post_photo.html', {'post': post})


def user_logout(request):
    logout(request)
    return redirect('home')
