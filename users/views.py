from random import choices
from string import ascii_lowercase, ascii_uppercase, digits

from django.contrib.auth import login
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        host = self.request.get_host()
        activation_url = f'http://{host}/users/confirm-email/{uid}/{token}'
        send_mail(
            'Подтверждение адреса электронной почты',
            f'Для подтверждения регистрации пройдите по ссылке {activation_url}',
            'skyproglazunov@yandex.ru',
            [user.email],  # Это поле "Кому" (можно указать список адресов)
            fail_silently=False,  # Сообщать об ошибках («молчать ли об ошибках?»)
        )
        return redirect('users:email_confirmation_sent')


def email_confirmation_sent(request):
    return render(request, 'users/email_confirmation_sent.html')


class UserConfirmEmailView(View):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('users:email_confirmed')
        else:
            return redirect('users:email_confirmation_failed')


def email_confirmed(request):
    return render(request, 'users/email_confirmed.html')


def email_confirmation_failed(request):
    return render(request, 'users/email_confirmation_failed.html')


def new_password(request):
    if request.method == 'POST':
        email_ = request.POST.get('email')
        user = User.objects.get(email=email_)
        sequence = choices(digits, k=9)
        sequence.extend(choices(ascii_lowercase, k=9))
        sequence.extend(choices(ascii_uppercase, k=9))
        new_password_ = ''.join(choices(sequence, k=9))
        user.set_password(new_password_)
        user.save()
        send_mail(
            'Востановление пароля',
            f'Новый пароль {new_password_}',
            'skyproglazunov@yandex.ru',
            [user.email],  # Это поле "Кому" (можно указать список адресов)
            fail_silently=False,  # Сообщать об ошибках («молчать ли об ошибках?»)
        )
    return render(request, 'users/password_reset.html')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('catalog:product_list')

    def get_object(self, queryset=None):
        return self.request.user
