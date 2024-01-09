from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Category, Question, Choice,QuizResult,Questionwithparts,Partsofquestion
from django.http import HttpResponse
from .forms import RegisterUserForm, ProfileForm
from django.db.models import Prefetch

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

def forms_page(request):

    return render(request, 'forms.html', {})
def quiz_view(request, category_id):

    # score = {
    #     1 : {
    #         "A" : 4,
    #         "B" : 3
    #     },
    #     2 : {
    #         "A" : 4,
    #         "B" : 3
    #     }
    # }

    # questions = Question.objects.filter(category_id=category_id)
    # choices=Choice.objects.filter(category_id=category_id)

    # return render(request, 'quiz.html', {'questions': questions,"choices":choices,"category_id":category_id ,"score":score[category_id]})
    if category_id==1 or category_id==2 :
        questions = Question.objects.filter(category_id=category_id)
        choices=Choice.objects.filter(category_id=category_id)
        return render(request, 'quiz.html', {'questions': questions,"choices":choices,"category_id":category_id})
    elif category_id==3 :
        questions = Question.objects.filter(category_id=category_id)
        choices1=Choice.objects.filter(category_id=category_id)
        choices2=Choice.objects.filter(category_id=5)
        return render(request, 'quiz2.html', {'questions': questions,"choices1":choices1,"choices2":choices2,"category_id":category_id})

    elif category_id==4 :
        questions = Questionwithparts.objects.filter(category_id=category_id)
        parts = Partsofquestion.objects.filter(question__in=questions)
        parts_prefetched = Prefetch('partsofquestion_set', queryset=parts, to_attr='parts')
        questions = questions.prefetch_related(parts_prefetched)
        choices=Choice.objects.filter(category_id=category_id)
        return render(request, 'quiz3.html', {'questions': questions,"choices":choices,"category_id":category_id})

       
    



# Create your views here.
def process_response(request):
    if request.method == 'POST':
        total_points = int(request.POST.get('total_points', 0))
        category_id=int(request.POST.get('category_id', 0))
        if category_id==1:
        # Perform further processing with the total points, for example, save it to the database
            if total_points<=10:
                mental_status='Ansiedad mínima o nula'
            elif total_points>10 and total_points<=20:
                mental_status='Ansiedad leve'
            elif total_points>20 and total_points<=30:
                mental_status='Ansiedad moderada'
            else:
                mental_status='Ansiedad severa'
            return HttpResponse(f'Mental Status: {mental_status} ')

        elif category_id==2:
            if total_points<=10:
                mental_status='Depresión mínima o nula'
            elif total_points>10 and total_points<=20:
                mental_status='Depresión  leve'
            elif total_points>20 and total_points<=30:
                mental_status='Depresión  moderada'
            else:
                mental_status='Depresión  severa'
            return HttpResponse(f'Mental Status: {mental_status} ')

        elif category_id==3:
            if 30<=total_points<=40:
                mental_status='Autoestima elevada'
            elif 26<=total_points<=29:
                mental_status='Autoestima media'
            else:
                mental_status='Autoestima baja '
            return HttpResponse(f'Mental Status: {mental_status} ')
        elif category_id==4:
            Categories=[]

            for i in range (1,8):
                c_key = f'c{i}'
                c_val = int(request.POST.get(f'c{i}', 0))
                Categories.append((c_key,c_val))



                # Categories.append(int(request.POST.get(f'c{i}', 0)))
            categories = sorted(Categories, key=lambda x: x[1])
            max_value = categories[-1][1]
            maxcat=categories[-1][0]
            second_max_value = categories[-2][1]
            secmaxcat=categories[-2][0]
            if maxcat=='c1':
                cat1="Ciencias y Tecnología"
            elif maxcat=='c2':
                cat1="Artes y Creatividad"
            elif maxcat=='c3':
                cat1="Ciencias Sociales y Humanidades"
            elif maxcat=='c4':
                cat1="Negocios y Emprendimiento"
            elif maxcat=='c5':
                cat1="Salud y Bienestar"
            elif maxcat=='c6':
                cat1="Servicio y Comunidad"
            else :
                cat1="Oficios y Técnicas Manuales"
            if secmaxcat=='c1':
                cat2="Ciencias y Tecnología"
            elif secmaxcat=='c2':
                cat2="Artes y Creatividad"
            elif secmaxcat=='c3':
                cat2="Ciencias Sociales y Humanidades"
            elif secmaxcat=='c4':
                cat2="Negocios y Emprendimiento"
            elif secmaxcat=='c5':
                cat2="Salud y Bienestar"
            elif secmaxcat=='c6':
                cat2="Servicio y Comunidad"
            else:
                cat2="Oficios y Técnicas Manuales"
            print(categories)
            print(max_value,second_max_value)
            print(cat1,cat2)
            return HttpResponse(f'Mental Status: {cat1} second_max_value: {cat2} ')
            
        # quiz_result = QuizResult(username=username,mental_status=mental_status)
        # quiz_result.save()
        # if request.user.is_authenticated:
        # # Access the user's ID
        #     user_id = request.user.id
        #     quiz_result = QuizResult(id=user_id,mental_status=mental_status,Category=category_id,date='2021-10-10')
        #     quiz_result.save()
        return HttpResponse(f'Mental Status: {mental_status} ')
    

    # Handle cases where the form is accessed via GET request
    return HttpResponse('This view only accepts POST requests.')
def chatbot(request):
    return render(request, 'chatbot.html')