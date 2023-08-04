from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from catalog.models import Product, Blog




class Productlistview(ListView):
    model = Product
    template_name = 'catalog/home.html'


# def home(request):
#     from catalog.models import Product
#     product_list = Product.objects.all()
#     context = {
#         'object_list': product_list
#     }
#     return render(request, 'catalog/home.html', context)
#


# def contacts(request):
#     if request.method == 'POST':
#             name = request.POST.get('name')
#             phone = request.POST.get('phone')
#             message = request.POST.get('message')
#             print(f'{name}, {phone}, {message}')
#     return render(request, 'catalog/contacts.html')


class Contactlistview(ListView):
    model = Product
    template_name = 'catalog/contacts.html'





# class ProductDetailView(ListView):
#     model = Product
#     template_name = 'catalog/good_detail.html'
#

# def good(request, pk):
#     from catalog.models import Product
#     catrgory_item = Product.objects.get(pk=pk)
#     context = {
#         'object_list':  catrgory_item
#     }
#     return render(request, 'catalog/good_detail.html', context)

class ProductByCategoryListView(DetailView):
    model = Product
    template_name = 'catalog/good_detail.html'

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(id=self.kwargs.get('pk'))
    #     return queryset
    #
    # def get_context_data(self, *args, **kwargs):
    #     context_data = super().get_context_data(*args, **kwargs)
    #     category_item = Product.objects.get(pk=self.kwargs.get('pk'))
    #     context_data['id'] = category_item
    #     return context_data

class Productcreateview(CreateView):
    model = Blog
    fields = ['title', 'content', 'preview']
    template_name = 'catalog/blog_form.html'
    success_url = reverse_lazy('home')

