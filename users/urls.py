from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, email_confirmation_sent, UserConfirmEmailView, email_confirmed, \
    email_confirmation_failed, new_password

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('email-confirmation-sent/', email_confirmation_sent, name='email_confirmation_sent'),
    path('confirm-email/<str:uidb64>/<str:token>/', UserConfirmEmailView.as_view(), name='confirm_email'),
    path('email-confirmed/', email_confirmed, name='email_confirmed'),
    path('confirm-email-failed/', email_confirmation_failed, name='email_confirmation_failed'),
    path('password_reset/', new_password, name='password_reset'),
]
