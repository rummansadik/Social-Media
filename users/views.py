from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from media.models import News
from django.views import View


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Your account has been created! You are now able to log in.')
            return redirect('login')

    else:
        form = UserRegistrationForm()
    news = News.objects.all().order_by('-date_posted')
    return render(request, 'users/register.html', {'form': form, 'news': news})


@login_required
def profile_edit(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(
                request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    news = News.objects.all().order_by('-date_posted')
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'news': news,
    }
    return render(request, 'users/profile_edit.html', context)


@login_required
def profile(request):
    news = News.objects.all().order_by('-date_posted')
    context = {
        'news': news,
    }
    return render(request, 'users/profile.html', context)
