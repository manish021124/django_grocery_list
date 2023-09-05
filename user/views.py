from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:        
        form = CreateUserForm(request.POST)

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Congratulation! You have created an account successfully. Pleae log in to continue.")
                return redirect('login')
                
        context = {'form': form}
        return render(request, 'signup.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:   
        if request.method == 'POST':   
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "You have logged in successfully.")
                return redirect('index')
            else:                
                messages.error(request, "Please enter correct username and password.")
              
        context = {}
        return render(request, 'login.html', context)


@login_required
def logoutUser(request):
    logout(request)
    messages.success(request, "You have logged out successfully.")
    return redirect('index')


@login_required
def deleteUser(request, username):
    username = request.user.username

    if request.method == 'POST':
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            user.delete()
            messages.success(request, "Your account has been deleted successfully.")
            return redirect('index')
        else:
            messages.error(request, "Please enter correct password.")

    context = {}
    return render(request, 'confirm_deletion.html', context)

    
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your data has been updated successfully.")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile.html', context)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your password has been changed successfully.")
            return redirect('index')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'change_password.html', {'form': form})




