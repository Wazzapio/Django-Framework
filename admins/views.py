from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from admins.forms import UserAdminCreateForm, UserAdminUpdateForm, CategoriesAdminCreateUpdateForm, \
    ProductsAdminCreateUpdateForm
from authapp.models import User
from mainapp.models import ProductCategory, Product


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'admins/admin.html')


def admin_users(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'admins/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
        else:
            messages.error(request, form.errors)
    else:
        form = UserAdminCreateForm()

    context = {
        'title': 'Geekshop - Админ | Регистрация',
        'form': form,
    }
    return render(request, 'admins/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_update(request, id):
    user_select = User.objects.get(id=id)

    if request.method == 'POST':
        form = UserAdminUpdateForm(data=request.POST, instance=user_select, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
        else:
            messages.error(request, form.errors)
    else:
        form = UserAdminUpdateForm(instance=user_select)

    context = {
        'title': 'Geekshop - Админ | Обновление',
        'form': form,
        'user_select': user_select,
    }
    return render(request, 'admins/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_delete(request, id):
    if request.method == 'POST':
        user = User.objects.get(id=id)
        user.is_active = False
        user.save()

    return HttpResponseRedirect(reverse('admins:admin_users'))


def admin_categories(request):
    context = {
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'admins/admin-categories-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_categories_create(request):
    if request.method == 'POST':
        form = CategoriesAdminCreateUpdateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_categories'))
    else:
        form = CategoriesAdminCreateUpdateForm()

    context = {
        'title': 'Geekshop - Категории | Создание',
        'form': form,
    }
    return render(request, 'admins/admin-categories-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_categories_update(request, id):
    category_select = ProductCategory.objects.get(id=id)

    if request.method == 'POST':
        form = CategoriesAdminCreateUpdateForm(data=request.POST, instance=category_select, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_categories'))
    else:
        form = CategoriesAdminCreateUpdateForm(instance=category_select)

    context = {
        'title': 'Geekshop - Категории | Обновление',
        'form': form,
        'category_select': category_select,
    }
    return render(request, 'admins/admin-categories-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_categories_delete(request, id):
    if request.method == 'POST':
        category = ProductCategory.objects.get(id=id)
        category.delete()

    return HttpResponseRedirect(reverse('admins:admin_categories'))


def admin_products(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'admins/admin-products-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_create(request):
    if request.method == 'POST':
        form = ProductsAdminCreateUpdateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_products'))
    else:
        form = ProductsAdminCreateUpdateForm()

    context = {
        'title': 'Geekshop - Продукты | Создание',
        'form': form,
    }
    return render(request, 'admins/admin-products-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_update(request, id):
    product_select = Product.objects.get(id=id)

    if request.method == 'POST':
        form = ProductsAdminCreateUpdateForm(data=request.POST, instance=product_select, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_products'))
    else:
        form = ProductsAdminCreateUpdateForm(instance=product_select)

    context = {
        'title': 'Geekshop - Продукты | Обновление',
        'form': form,
        'product_select': product_select,
    }
    return render(request, 'admins/admin-products-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_delete(request, id):
    if request.method == 'POST':
        product = Product.objects.get(id=id)
        product.delete()

    return HttpResponseRedirect(reverse('admins:admin_products'))
