from django.urls import path
from . import views
from .views import quiz_view, process_response,chatbot,get_videos

urlpatterns = [
    path('auth/login', views.login_user, name='login'),
    path('auth/logout', views.logout_user, name='logout'),
    path('auth/register', views.register_user, name='register'),
    path('', views.home_page, name='home'),
    path('about/', views.about_page, name='about'),
    path('faq/', views.faq_page, name='faq'),
    path('forms/', views.forms_page, name='forms'),
    path('quiz/<int:category_id>', quiz_view, name='quiz_view'),
    path('quiz/process_response', process_response, name='process_response'),
    path('chatbot/', views.chatbot, name='quiz_results'),
    path('footer/',views.get_videos,name='footer')
]
