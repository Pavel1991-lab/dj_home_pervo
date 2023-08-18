from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.shortcuts import redirect
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, View
from django.core.mail import send_mail
from users.models import User

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
        send_mail(
            subject= 'Поздравляем с регистарцией',
            message= 'Вы зарегистрировались',
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [new_user.email]

        )

        # send_mail_for_verify(request)
        # return redirect('confirm email')
        #

        return super().form_valid(form)



# class  EmailVerify(View):
#     pass

