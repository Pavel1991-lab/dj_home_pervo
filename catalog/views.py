from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from catalog.models import Product, Version, Category
from pytils.translit import slugify
from catalog.services import get_category_cache
from catalog.forms import ProductForm, VersionForm, ModeratorProductForm
from rest_framework.permissions import BasePermission

from rest_framework.exceptions import PermissionDenied




# class IsEnrolled(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return obj.user == request.user



class Productlistview(ListView):
    model = Product
    template_name = 'catalog/home.html'


class Contactlistview(ListView):
    model = Product
    template_name = 'catalog/contacts.html'


class ProductByCategoryListView(DetailView):
    model = Product
    template_name = 'catalog/good_detail.html'

# @login_required
class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        description = form.cleaned_data.get('description')

        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']

        for word in forbidden_words:
            if word in name.lower() or word in description.lower():
                form.add_error(None, f"Запрещенное слово '{word}' найдено в названии или описании продукта.")
                return self.form_invalid(form)

        # Устанавливаем текущего пользователя как владельца продукта
        form.instance.user = self.request.user

        return super().form_valid(form)


# @login_required
class Http401:
    pass


class ProductUpdateview(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'product.can_change_desc_permission'
    def get_form_class(self):
        if self.request.user.is_staff:
            return ModeratorProductForm
        return ProductForm

    def has_permission(self):
        obj = self.get_object()
        if self.request.user == obj.user or self.request.user.is_staff:
            return True
        return super().has_permission()


    # def dispatch(self, request, *args, **kwargs):
    #     obj = self.get_object()
    #     if obj.user != self.request.user and not (self.request.user.is_superuser or self.request.user.is_staff):
    #         raise Http401("У вас нет прав для редактирования этого продукта")
    #     return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):

        form.instance.user = self.request.user


        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            self.object.email = self.request.user
            formset.save()


        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormSet = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        context_data['formset'] = VersionFormSet
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormSet(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormSet(instance=self.object)

        return context_data

    def your_view(request):
        registered_by = request.user.email

        return registered_by


class CategoryListView(ListView):
    model = Category

    def get_queryset(self):
        if settings.CACHE_ENABLED:
            category_list = get_category_cache()
            return category_list
        return super().get_queryset()



