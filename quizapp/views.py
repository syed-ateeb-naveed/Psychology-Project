from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterUserForm, ProfileForm
# Create your views here.

def login_user(request):

    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            
            return redirect('home')
        else:
            messages.success(request, ("There was an error logging in :(("))
            return redirect('login')

    return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out"))

    return redirect('home')

@login_required
def homepage(request):

    return render(request, 'home.html', {})

def register_user(request):

    if request.method == "POST":
        user_form = RegisterUserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            email = user_form.cleaned_data['email']
            password = user_form.cleaned_data['password1']
            user = authenticate(email=email, password=password)
            login(request, user)
            messages.success(request, ("Registrations Successfull"))
            return redirect('home')
    else:
        user_form = RegisterUserForm()
        profile_form = ProfileForm()

    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form})