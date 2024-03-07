from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Category, Question, Choice,Result,Questionwithparts,Partsofquestion
from django.http import HttpResponse
from .forms import RegisterUserForm, ProfileForm
from django.db.models import Prefetch
from googleapiclient.discovery import build
from django.http import JsonResponse
from datetime import datetime
from datetime import timedelta

from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView, PasswordResetCompleteView, PasswordResetConfirmView
from django.urls import reverse_lazy

User = get_user_model()
# Create your views here.
api_key = 'AIzaSyDtqvCUJJhv6N7DBJrXI7lyzwjsCYPCiy4'
youtube = build('youtube', 'v3', developerKey=api_key)


class CustomPasswordResetView(PasswordResetView):
    subject_template_name = 'password_reset_subject.txt'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Tu contraseña se ha restablecido")
        return response
    
# class CustomPasswordResetCompleteView(PasswordResetCompleteView):
#       # Specify your custom template name

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['custom_message'] = "Tu contraseña se ha restablecido"  # Add your custom message to the context
#         return context

    
def login_user(request):

    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            
            return redirect('enduser')
        else:
            messages.success(request, ("There was an error logging in :(("))
            return redirect('login')

    return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out"))

    return redirect('home')

# def reset_password(request):
#     if request.method == "POST":
#         message = "Hi"
#         email = request.POST['email']
#         try:
#             user = User.objects.get(email=email)
#         except User.DoesNotExist:
#             messages.error(request, "Email does not exist.")
#             return redirect('passwordReset')
#         subject = "OTP for Password Reset"
#         send_mail(
#             subject,
#             message,
#             "Ateeb <ateebnaveed1996@gmail.com>",
#             [email],
#             fail_silently=False
#         )

#         messages.success(request, ("Email sent successfully !"))

#     return render(request, 'reset.html', {})

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
    if request.user.is_authenticated:
        user_id = User.objects.get(id=request.user.id)
        category_id=4
        chk=take_quiz(request,user_id,category_id)
        if chk != None:
            return chk    
    
    return render(request, 'oriention.html', {})


def about_us(request):

    return render(request, 'about_us.html', {})
def anxiety(request):
    if request.user.is_authenticated:
        user_id = User.objects.get(id=request.user.id)
        category_id=1
        chk=take_quiz(request,user_id,category_id)
        if chk != None:
            return chk
      
    return render(request, 'anxiety.html', {})
def autostima(request):
    if request.user.is_authenticated:
        user_id = User.objects.get(id=request.user.id)
        category_id=3
        chk=take_quiz(request,user_id,category_id)
        if chk != None:
            return chk    
    return render(request, 'autostima.html', {})
def contact_us(request):

    return render(request, 'contact_us.html', {})
def depression(request):
    if request.user.is_authenticated:
        user_id = User.objects.get(id=request.user.id)
        category_id=2
        chk=take_quiz(request,user_id,category_id)
        if chk != None:
            return chk    
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

    return render(request, 'terms_&_conditions.html', {})
def quiz_view(request, category_id):

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

def process_response(request):

    if request.method == 'POST':
        total_points = int(request.POST.get('total_points', 0))
        category_id=int(request.POST.get('category_id', 0))
        if category_id==1:
        # Perform further processing with the total points, for example, save it to the database
            if total_points<=10:
                mental_status='Ansiedad mínima o nula: Un resultado en este rango no necesariamente indica ausencia total de preocupaciones o estrés. Es normal experimentar algún grado de ansiedad en respuesta a situaciones cotidianas. Sin embargo, un nivel bajo en el inventario sugiere que estos no son prominentes o problemáticos.'
            elif total_points>10 and total_points<=20:
                mental_status='Ansiedad leve: Este resultado indica que la persona puede estar experimentando algunos síntomas de ansiedad, pero estos son leves y probablemente no interfieran de manera significativa con sus actividades diarias. Sin embargo, el resultado puede fungir como un punto de partida para la discusión sobre estrategias de manejo de estrés y ansiedad.'
            elif total_points>20 and total_points<=30:
                mental_status='Ansiedad moderada: Esta puntuación indica que la persona está experimentando una cantidad significativa de síntomas de ansiedad. Esto significa que la ansiedad está presente y es notable, pero no necesariamente abrumadora o incapacitante. Una puntuación moderada puede sugerir la necesidad de una evaluación más profunda por parte de un profesional de la salud mental.'
            else:
                mental_status='Ansiedad severa: Las personas con puntuaciones en el rango severo pueden presentar síntomas como preocupaciones y miedos extremos, pánico, dificultad para respirar, mareos, temblores, y un estado constante de hiperactividad del sistema nervioso. Se recomienda que las personas con una puntuación severa busquen la evaluación y el tratamiento de un profesional de la salud mental, ya que pueden beneficiarse de terapias específicas, apoyo y posiblemente medicación para manejar sus síntomas.'
            result(request,mental_status,category_id)
            return render(request, 'result_anxiety.html', {'mental_status':mental_status})
        elif category_id==2:
            if total_points<=10:
                mental_status='Depresión mínima o nula: Una puntuación en este rango sugiere que la persona presenta muy pocos o ningún síntoma de depresión significativo. Esto puede interpretarse como una indicación de que actualmente no se está experimentando depresión clínica.'
            elif total_points>10 and total_points<=20:
                mental_status='Depresión leve: Una puntuación en este rango significa que la persona puede estar experimentando síntomas que no son lo suficientemente severos como para constituir un episodio depresivo mayor. Sin embargo, puede ser un indicador para realizar una evaluación más profunda.'
            elif total_points>20 and total_points<=30:
                mental_status='Depresión moderada: Este rango indica que la persona está experimentando varios síntomas de depresión, como tristeza persistente, problemas de autoestima, dificultades de concentración y cambios en el sueño o el apetito, con un impacto moderado en su funcionamiento diario.'
            else:
                mental_status='Depresión severa: Los individuos con una puntuación en este rango suelen experimentar una amplia gama de síntomas graves de depresión, posibles pensamientos de autolesión o suicidio, y otros síntomas que impactan considerablemente en su bienestar y capacidad para realizar actividades diarias.'
            result(request,mental_status,category_id)

            return render(request, 'result_depression.html', {'mental_status':mental_status})       
        elif category_id==3:
            if 30<=total_points<=40:
                mental_status='Autoestima elevada. Esta puntuación refleja una actitud general de aceptación y satisfacción con uno mismo, y sugiere que la persona se siente competente para enfrentar los desafíos de la vida. Las personas con autoestima elevada suelen mostrar resiliencia frente a las adversidades y tienden a tener una perspectiva optimista de sus capacidades y su valía personal.'
            elif 26<=total_points<=29:
                mental_status='Autoestima media. La persona puede tener una visión positiva de sus propias capacidades y valor en algunas áreas, mientras que en otras puede tener dudas o ser crítica consigo misma. Una autoestima media sugiere que la persona ni se sobrevalora ni se infravalora de manera consistente, y su nivel de satisfacción consigo misma podría ser influenciado por las circunstancias.'
            else:
                mental_status='Autoestima baja. Este resultado indica que la persona tiene una percepción negativa de sí misma. Esto se manifiesta en una tendencia a ver sus propias capacidades y valor personal de manera crítica y posiblemente poco realista. La persona puede sentir que no cumple con sus propias expectativas o las de otros, y puede tener dificultades para reconocer sus logros y cualidades positivas. '
            result(request,mental_status,category_id)

            return render(request, 'result_autostima.html', {'mental_status':mental_status})
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
                cat1="Ciencias y Tecnología: Esta categoría indica que la persona podría encontrar satisfacción y éxito en ambientes que se enfocan en la innovación, la resolución de problemas técnicos, el análisis lógico, y el trabajo con tecnologías avanzadas."
            elif maxcat=='c2':
                cat1="Artes y Creatividad: Esta categoría indica una marcada preferencia y entusiasmo por actividades y carreras relacionadas con la expresión artística y la creatividad. La persona podría disfrutar y sobresalir en entornos que valoran la originalidad, la expresión personal y la exploración de ideas a través de medios artísticos y creativos."
            elif maxcat=='c3':
                cat1="Ciencias Sociales y Humanidades: Esta categoría indica que la persona podría encontrar satisfacción y éxito en profesiones o estudios que se centran en el análisis de fenómenos sociales, la educación, o el compromiso con causas sociales y culturales."
            elif maxcat=='c4':
                cat1="Negocios y Emprendimiento: Esta categoría indica una marcada inclinación y entusiasmo por actividades y carreras relacionadas con el mundo empresarial.  La persona podría disfrutar y sobresalir en entornos que valoran la toma de decisiones estratégicas, la innovación en los negocios, el liderazgo, y la gestión de proyectos y recursos."
            elif maxcat=='c5':
                cat1="Salud y Bienestar: Esta categoría indica que la persona podría encontrar satisfacción y éxito en profesiones o estudios enfocados en la asistencia sanitaria, el apoyo terapéutico, la promoción de estilos de vida saludables y el cuidado directo de pacientes o clientes."
            elif maxcat=='c6':
                cat1="Servicio y Comunidad: Esta categoría indica que la persona podría disfrutar y sobresalir en entornos que valoran la contribución al bienestar social, la asistencia a personas en necesidad, el involucramiento en la comunidad y la promoción del cambio social positivo."
            else :
                cat1="Oficios y Técnicas Manuales: Esta categoría indica una marcada preferencia por carreras y actividades que implican habilidades prácticas, trabajo manual y técnico. Esto incluye áreas como carpintería, construcción, electricidad, electrónica y mecánica automotriz."
            if secmaxcat=='c1':
                cat2="Ciencias y Tecnología: Esta categoría indica que la persona podría encontrar satisfacción y éxito en ambientes que se enfocan en la innovación, la resolución de problemas técnicos, el análisis lógico, y el trabajo con tecnologías avanzadas."
            elif secmaxcat=='c2':
                cat2="Artes y Creatividad: Esta categoría indica una marcada preferencia y entusiasmo por actividades y carreras relacionadas con la expresión artística y la creatividad. La persona podría disfrutar y sobresalir en entornos que valoran la originalidad, la expresión personal y la exploración de ideas a través de medios artísticos y creativos."
            elif secmaxcat=='c3':
                cat2="Ciencias Sociales y Humanidades: Esta categoría indica que la persona podría encontrar satisfacción y éxito en profesiones o estudios que se centran en el análisis de fenómenos sociales, la educación, o el compromiso con causas sociales y culturales."
            elif secmaxcat=='c4':
                cat2="Negocios y Emprendimiento: Esta categoría indica una marcada inclinación y entusiasmo por actividades y carreras relacionadas con el mundo empresarial.  La persona podría disfrutar y sobresalir en entornos que valoran la toma de decisiones estratégicas, la innovación en los negocios, el liderazgo, y la gestión de proyectos y recursos."
            elif secmaxcat=='c5':
                cat2="Salud y Bienestar: Esta categoría indica que la persona podría encontrar satisfacción y éxito en profesiones o estudios enfocados en la asistencia sanitaria, el apoyo terapéutico, la promoción de estilos de vida saludables y el cuidado directo de pacientes o clientes."
            elif secmaxcat=='c6':
                cat2="Servicio y Comunidad: Esta categoría indica que la persona podría disfrutar y sobresalir en entornos que valoran la contribución al bienestar social, la asistencia a personas en necesidad, el involucramiento en la comunidad y la promoción del cambio social positivo."
            else :
                cat2="Oficios y Técnicas Manuales: Esta categoría indica una marcada preferencia por carreras y actividades que implican habilidades prácticas, trabajo manual y técnico. Esto incluye áreas como carpintería, construcción, electricidad, electrónica y mecánica automotriz."
            
            mental_status=cat1+" & "+cat2
            result(request,mental_status,category_id)
            return render(request, 'result_oriention.html', {'cat1':cat1,'cat2':cat2})            

        
    

    # Handle cases where the form is accessed via GET request
def result(request,mental_status,category_id):
    if request.user.is_authenticated:
        # Access the user's ID
            print('result updated')
            user_id = User.objects.get(id=request.user.id)
            today_date = datetime.now().date()
            category_id=Category.objects.get(id=category_id)
            quiz_result = Result(user=user_id,mental_status=mental_status,category=category_id,date=today_date)
            quiz_result.save()
    else:
        print("no user logged in")



def chatbot(request):
    return render(request, 'chatbot.html')

def get_videos(request):
    channel_id = 'UCpeW5jO3i-jf_9I6SyitoOA'
# Extracted from the provided YouTube channel link
    latest_video_response = youtube.search().list(
        part='id',
        channelId=channel_id,
        order='date',
        type='video',
        maxResults=1
    ).execute()

    video_id = latest_video_response['items'][0]['id']['videoId']
    most_viewed_video_response = youtube.search().list(
        part='id',
        channelId=channel_id,
        order='viewCount',
        type='video',
        maxResults=1
    ).execute()

    video_id2 = most_viewed_video_response['items'][0]['id']['videoId']
    videos=[video_id,video_id2]
    videos = {'latest_video': video_id, 'most_viewed_video': video_id2}

    return JsonResponse(videos)

def take_quiz(request,user_id,category_id):
    # Get the current date
    today = datetime.now().date()
    # Get the user's result if available
    try:
        user_result = Result.objects.get(user=user_id, category=category_id)
        test_date = user_result.date.date()
        # Calculate the difference between today's date and the test date
        days_difference = (today - test_date).days
        if days_difference <= 180:
            # Calculate the minimum date the user can retake the quiz
            eligible_date = test_date + timedelta(days=180)
            error_message = f"You can only take the quiz on or after {eligible_date.strftime('%d-%m-%Y')}"
            messages.error(request, error_message)
            return render(request, 'enduser.html', {'cat_id': category_id})
        else:
            # Allow the user to take the quiz
            empty=''
            return empty
    except Result.DoesNotExist:
        # If user has not taken the test, allow them to take the quiz
        return None

def display_result(request,cat_id):
    user_id = User.objects.get(id=request.user.id)
    user_result = Result.objects.get(user=user_id, category=cat_id)
    mental_status=user_result.mental_status
    if cat_id==1:
        return render(request, 'result_anxiety.html', {'mental_status':mental_status})
    elif cat_id==2:
        return render(request, 'result_depression.html', {'mental_status':mental_status})
    elif cat_id==3:
        return render(request, 'result_autostima.html', {'mental_status':mental_status})
    elif cat_id==4:
        tmp=mental_status.split("&")
        print(tmp)
        cat1=tmp[0]
        cat2=tmp[1]
        return render(request, 'result_oriention.html', {'cat1':cat1,'cat2':cat2})
    else:
        return None


