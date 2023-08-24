import secrets
from random import random
from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import CreateView
from django.core.mail import send_mail
from users.models import User
from django.contrib import messages
from users.forms import UserForm




# from users.utils import send_mail_for_verify


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('catalog:product_list')
    template_name = "users/register.html"



    def form_valid(self, form):
        new_user = form.save()
        new_user.verification_key = secrets.randbelow(1_000_000)
        new_user.save()

        token = urlsafe_base64_encode(force_bytes(new_user.verification_key))
        verification_url = reverse('users:verify', kwargs={'token': token})
        send_mail(
            subject='Регистрация на Портале.',
            message=f'Для подтвердения регистрации, пройдите по ссылке ниже в письме. \n {self.request.build_absolute_uri(verification_url)}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)


        return super().form_valid(form)


def verify_email(request, token):
    try:
        user_verification_key = urlsafe_base64_decode(token).decode()
        user = User.objects.get(verification_key=user_verification_key)
        if int(user_verification_key) == user.verification_key:
            user.is_active = True
            user.save()
            messages.success(request, 'Ваш аккаунт был успешно подтвержден. Теперь вы можете войти.')
            return redirect('catalog:category')
        else:
            messages.error(request, 'Ошибка верификации аккаунта.')
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        messages.error(request, 'Ошибка верификации аккаунта.')


def generate_password(request):
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    request.user.set_password(new_password)

    send_mail(
        subject='Смена Пароля',
        message=f'Ваш новый пароль \n {new_password}',
        from_email=None,
        recipient_list=[request.user.email]
    )
    request.user.save()
    return redirect(reverse('catalog:product_list'))