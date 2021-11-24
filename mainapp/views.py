from django.shortcuts import render
from mainapp.models import ProductCategory, Product

# Create your views here.

def index(request):
    context = {
        'title': 'geekshop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'geekshop | Продукты',
    }

    context['products'] = Product.objects.all()
    context['categories'] = ProductCategory.objects.all()

    return render(request, 'mainapp/products.html', context)
