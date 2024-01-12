from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import quiz_view, process_response,chatbot,get_videos

urlpatterns = [
    path('auth/login', views.login_user, name='login'),
    path('auth/logout', views.logout_user, name='logout'),
    path('auth/register', views.register_user, name='register'),
    # path('auth/reset', views.reset_password, name='passwordReset'),
    path('', views.home_page, name='home'),
    path('about/', views.about_page, name='about'),
    path('faq/', views.faq_page, name='faq'),
    path('forms/', views.forms_page, name='forms'),
    path('quiz/<int:category_id>', quiz_view, name='quiz_view'),
    path('quiz/process_response', process_response, name='process_response'),
    path('chatbot/', views.chatbot, name='quiz_results'),
    path('footer/',views.get_videos,name='footer'),

    #reset views
    path('auth/reset', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('auth/reset_sent', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('auth/reset_complete', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
