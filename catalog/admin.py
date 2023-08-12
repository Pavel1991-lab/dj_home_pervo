from django.contrib import admin

from catalog.models import Category, Product, Version


# Register your models here.


@admin.register(Category)
class Categoryadmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description')

@admin.register(Product)
class Categoryadmin(admin.ModelAdmin):
    list_display = ('pk', 'name',  'purchase_price', 'category', 'description')
    list_filter = ('category',)
    search_fields = ('name', 'description')

@admin.register(Version)
class Versionadmin(admin.ModelAdmin):
    list_display = ('product', 'version_number', 'version_name', 'is_active')
    list_filter = ('product',)

