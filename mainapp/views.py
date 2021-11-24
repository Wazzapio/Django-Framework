from django.shortcuts import render
from mainapp.models import ProductCategory, Product

# Create your views here.

def index(request):
    context = {
        'title': 'geekshop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    allCategories = ProductCategory.objects.all()
    allProducts = Product.objects.all()

    context = {
        'title': 'geekshop - Продукты',
    }
    context['categories'] = allCategories
    context['products'] = allProducts

    return render(request, 'mainapp/products.html', context)
