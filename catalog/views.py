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

class ProductUpdateview(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

