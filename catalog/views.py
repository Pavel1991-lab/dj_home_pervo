from django.shortcuts import render

# Create your views here.


def home(request):
    from catalog.models import Product
    product_list = Product.objects.all()
    context = {
        'object_list': product_list
    }
    return render(request, 'catalog/home.html', context)



def contacts(request):
    if request.method == 'POST':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            print(f'{name}, {phone}, {message}')
    return render(request, 'catalog/contacts.html')


def good(request, pk):
    from catalog.models import Product
    catrgory_item = Product.objects.get(pk=pk)
    context = {
        'object_list':  catrgory_item
    }
    return render(request, 'catalog/good.html', context)