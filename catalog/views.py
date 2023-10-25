from django.shortcuts import render

from catalog.models import Product


def home(request):
    product_list = Product.objects.all()
    context = {
        "object_list": product_list,
        "title": 'Каталог'
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')

    return render(request, 'catalog/contacts.html')


def product(request, pk):
    product_obj = Product.objects.get(id=pk)
    context ={
        'object': product_obj
    }
    return render(request, 'catalog/product.html', context)
