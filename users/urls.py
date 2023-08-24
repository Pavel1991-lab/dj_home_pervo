from django.urls import path
from django.views.generic import TemplateView

from users.apps import UsersConfig

from users.views import LoginView, LogoutView, RegisterView, verify_email
# EmailVerify

app_name = UsersConfig.name

urlpatterns = [

    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verify/<str:token>/', verify_email, name='verify'),
    # path('activate/<str:token>/', activate_user, name='activate_user'),
    # path('confirm_email/', TemplateView.as_view(template_name='users/confirm_email'), name='confirm_email'),
    # path('verify_email/<uidb64>/<token>', EmailVerify.as_view(), name='verify_emaile')
]