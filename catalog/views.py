from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from catalog.models import Product
from pytils.translit import slugify

from catalog.forms import ProductForm


class Productlistview(ListView):
    model = Product
    template_name = 'catalog/home.html'


class Contactlistview(ListView):
    model = Product
    template_name = 'catalog/contacts.html'


class ProductByCategoryListView(DetailView):
    model = Product
    template_name = 'catalog/good_detail.html'


class ProductCreate(CreateView):
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

        return super().form_valid(form)

class ProductUpdateview(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

