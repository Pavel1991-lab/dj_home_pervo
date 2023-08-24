import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.crypto import get_random_string

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")

    avatar = models.ImageField(upload_to='users/', verbose_name='аватар')
    phone_number = models.CharField(max_length=20, verbose_name= 'номер телефона')
    country = models.CharField(max_length=100, verbose_name= 'страна')

    verification_key = models.CharField(max_length=255, blank=True, null=True, verbose_name='ключ верификации')



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []