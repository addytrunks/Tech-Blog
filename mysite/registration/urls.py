from django.urls import path
from .views import UserRegistrationView
from django.contrib.auth import views as auth_views

app_name = 'reg'

#create your paths here
urlpatterns = [

    path('register/',UserRegistrationView.as_view(),name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='registration/logut.html'),name='logout'),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"),
     name="password_reset"),

    path('reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"),
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"),
     name="password_reset_confirm"),

    path('reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"),
        name="password_reset_complete"),









]
