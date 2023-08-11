from django.db import models



class Fidbeck(models.Model):
    title = models.CharField(max_length=100, verbose_name='название', unique=True)
    slug = models.CharField(max_length=150, verbose_name='slug', null=True, blank=True)
    content = models.TextField(verbose_name='содержимое', unique=True)
    preview = models.ImageField(upload_to='product_images', blank=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


    views_count = models.IntegerField(default=0, verbose_name='просмотры')
    is_published = models.BooleanField(default=True)



