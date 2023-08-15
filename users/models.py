from django.contrib.auth.models import AbstractUser
from django.db import models




class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")

    avatar = models.ImageField(upload_to='users/', verbose_name='аватар')
    phone_number = models.CharField(max_length=20, verbose_name= 'номер телефона')
    country = models.CharField(max_length=100, verbose_name= 'страна')




    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


