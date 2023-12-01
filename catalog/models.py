
from django.conf import settings
from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    description = models.TextField(verbose_name='описание')

class Product(models.Model):
    ACTIVE_CHOICES = (
        ('yes', 'Активна'),
        ('no', 'Не активна'),
    )
    name = models.CharField(max_length=100, verbose_name='название')  # наименование
    description = models.TextField(verbose_name='описание')  # описание
    image = models.ImageField(upload_to='product_images', blank=True, null=True)  # изображение (превью)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')  # цена за покупку
    created_date = models.DateTimeField(auto_now_add=True)  # дата создания
    last_modified_date = models.DateTimeField(auto_now=True)  # дата последнего изменения
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, verbose_name='пользователь')
    is_published = models.CharField(default=False, choices=ACTIVE_CHOICES, verbose_name='опубликовано')

    class Meta:
        verbose_name = 'Расслыка'

        permissions = [
            ('can_change_product', 'Can_change_product'),
        ]


class Version(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.CharField(max_length=20, verbose_name='номер версии')
    version_name = models.CharField(max_length=100, verbose_name='имя версии')
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.version_name