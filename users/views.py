from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.core.mail import send_mail
from users.models import User

from users.forms import UserForm


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

        return super().form_valid(form)





