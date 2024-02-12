from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import quiz_view, process_response, chatbot, get_videos, CustomPasswordResetView, CustomPasswordResetConfirmView

urlpatterns = [
    path('auth/login', views.login_user, name='login'),
    path('auth/logout', views.logout_user, name='logout'),
    path('auth/register', views.register_user, name='register'),
    # path('auth/reset', views.reset_password, name='passwordReset'),
    path('', views.home_page, name='home'),
    # path('about/', views.about_page, name='about'),
    # path('faq/', views.faq_page, name='faq'),
    # path('forms/', views.forms_page, name='forms'),
    path('quiz/<int:category_id>', quiz_view, name='quiz_view'),
    path('quiz/process_response', process_response, name='process_response'),
    path('chatbot/', views.chatbot, name='quiz_results'),
    path('footer/',views.get_videos,name='footer'),

    #reset views
    path('auth/reset', CustomPasswordResetView.as_view(template_name="reset_password.html", html_email_template_name="reset_password_email.html"), name="reset_password"),
    path('auth/reset_sent', auth_views.PasswordResetDoneView.as_view(template_name="reset_done.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>', CustomPasswordResetConfirmView.as_view(template_name="reset_confirm.html"), name="password_reset_confirm"),
    # path('auth/reset_complete', CustomPasswordResetCompleteView.as_view(), name="password_reset_complete"),
    # pages
    path('oriention/', views.oriention, name='oriention'),
    path('about/', views.about_us, name='about'),
    path('anxiety/', views.anxiety, name='anxiety'),
    path('autostima/', views.autostima, name='autostima'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('depression/', views.depression, name='depression'),
    path('enduser/', views.enduser, name='enduser'),
    path('faq/', views.faq, name='faq'),
    path('forms/', views.forms, name='forms'),
    path('function/', views.function, name='function'),
    path('generate_new_password/', views.generate_new_password, name='generate_new_password'),
    path('how_do_you_feel/', views.how_do_you_feel, name='how_do_you_feel'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('term_&_condition/', views.termscondition, name='term_&_condition'),
    path('result_anxiety/', views.result_anxiety, name='result_anxiety'),
    path('result_autostima/', views.result_autostima, name='result_autostima'),
    path('result_depression/', views.result_depression, name='result_depression'),
    path('result_oriention/', views.result_oriention, name='result_oriention'),
                





]
