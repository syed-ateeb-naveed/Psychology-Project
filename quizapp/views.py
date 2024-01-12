from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterUserForm, ProfileForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()
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

def reset_password(request):
    if request.method == "POST":
        message = "Hi"
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "Email does not exist.")
            return redirect('passwordReset')
        subject = "OTP for Password Reset"
        send_mail(
            subject,
            message,
            "Ateeb <ateebnaveed1996@gmail.com>",
            [email],
            fail_silently=False
        )

        messages.success(request, ("Email sent successfully !"))

    return render(request, 'reset.html', {})

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

def home_page(request):

    return render(request, 'home.html', {})

def about_page(request):

    return render(request, 'about.html', {})

def faq_page(request):

    return render(request, 'faq.html', {})


def oriention(request):

    return render(request, 'oriention.html', {})


def about_us(request):

    return render(request, 'about_us.html', {})
def anxiety(request):

    return render(request, 'anxiety.html', {})
def autostima(request):

    return render(request, 'autostima.html', {})
def contact_us(request):

    return render(request, 'contact_us.html', {})
def depression(request):

    return render(request, 'depression.html', {})
def enduser(request):

    return render(request, 'enduser.html', {})
def faq(request):

    return render(request, 'faq.html', {})
def forms(request):

    return render(request, 'forms.html', {})
def function(request):

    return render(request, 'function.html', {})
def generate_new_password(request):

    return render(request, 'generate_new_password.html', {})
def how_do_you_feel(request):

    return render(request, 'how_do_you_feel.html', {})
def privacy_policy(request):

    return render(request, 'privacy_policy.html', {})
def result_anxiety(request):

    return render(request, 'result_anxiety.html', {})
def result_depression(request):

    return render(request, 'result_depression.html', {})
def result_oriention(request):

    return render(request, 'result_oriention.html', {})

def result_autostima(request):

    return render(request, 'result_autostima.html', {})

def  termscondition(request):

    return render(request, 'terms_&_condition.html', {})