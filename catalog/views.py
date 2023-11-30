from django.shortcuts import render

from catalog.models import Product, Category



def index(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Главная'
    }
    return render(request, 'catalog/index.html', context)


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')

    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contact.html', context)


def product(request, pk):
    context = {
        'object': Product.objects.get(pk=pk)
    }
    return render(request, 'catalog/product.html', context)


def category_index(request):
    category_all = Category.objects.all()
    context = {
        'category_list': category_all,
        'title': 'Категории'
    }
    return render(request, 'catalog/category_list.html', context)
