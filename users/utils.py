from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


# from django.core.mail import EmailMessage
# from django.template.loader import render_to_string
#
# def send_mail_for_verify(request, token_generator, user):
#     message = render_to_string('users/verify_email.html', {
#         'user': user,
#         'domain': request.get_host(),
#         'token': token_generator.make_token(user),
#     })
#     email = EmailMessage(
#         'Verify Email',
#         message,
#         from_email='your_email@example.com',
#         to=[user.email]
#     )
#     email.send()