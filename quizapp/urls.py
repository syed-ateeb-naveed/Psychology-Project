from django.urls import path
from . import views

urlpatterns = [
    path('auth/login', views.login_user, name='login'),
    path('auth/logout', views.logout_user, name='logout'),
    path('auth/register', views.register_user, name='register'),
    path('', views.home_page, name='home'),
    path('about/', views.about_page, name='about'),
    path('faq/', views.faq_page, name='faq'),
    path('forms/', views.forms_page, name='forms'),
]
