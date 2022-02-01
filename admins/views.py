from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404, render

from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, TemplateView

from admins.forms import UserAdminCreateForm, UserAdminUpdateForm, CategoriesAdminCreateUpdateForm, \
    ProductsAdminCreateUpdateForm
from authapp.models import User
from mainapp.mixin import BaseClassContextMixin, CustomDispatchMixin
from mainapp.models import ProductCategory, Product


class UserTemplateView(TemplateView, CustomDispatchMixin):
    template_name = 'admins/admin.html'


class UserListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-read.html'
    title = 'Админка | Пользователи'


class UserCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminCreateForm
    success_url = reverse_lazy('admins:admin_users')
    title = 'Админка | Создать пользователя'

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, files=request.FILES)
        if form.is_valid():
            messages.set_level(request, messages.SUCCESS)
            messages.success(request, 'Новый пользователь успешно создан!')
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
        else:
            messages.error(request, form.errors)
            return HttpResponseRedirect(reverse('admins:admin_users_create'))


class UserUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminUpdateForm
    success_url = reverse_lazy('admins:admin_users')
    title = 'Админка | Редактирование пользователя'


class UserActivateView(DeleteView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    success_url = reverse_lazy('admins:admin_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active == False:
            self.object.is_active = True
            self.object.save()
            return HttpResponseRedirect(self.get_success_url())
        return HttpResponseRedirect(self.get_success_url())


class UserDeleteView(DeleteView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class CategoriesListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-categories-read.html'
    title = 'Админка | Категории'


class CategoriesCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-categories-create.html'
    form_class = CategoriesAdminCreateUpdateForm
    success_url = reverse_lazy('admins:admin_categories')
    title = 'Админка | Создать категорию'

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            messages.set_level(request, messages.SUCCESS)
            messages.success(request, 'Новая категория успешно создана!')
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_categories'))
        else:
            messages.error(request, form.errors)
            return HttpResponseRedirect(reverse('admins:admin_categories_create'))


class CategoriesUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-categories-update-delete.html'
    form_class = CategoriesAdminCreateUpdateForm
    success_url = reverse_lazy('admins:admin_categories')
    title = 'Админка | Редактирование категории'


class CategoriesActivateView(DeleteView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    success_url = reverse_lazy('admins:admin_categories')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active == False:
            self.object.is_active = True
            self.object.save()
            return HttpResponseRedirect(self.get_success_url())
        return HttpResponseRedirect(self.get_success_url())


class CategoriesDeleteView(DeleteView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    success_url = reverse_lazy('admins:admin_categories')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ProductsListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-read.html'
    title = 'Админка | Продукты'


class ProductsCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-create.html'
    form_class = ProductsAdminCreateUpdateForm
    success_url = reverse_lazy('admins:admin_products')
    title = 'Админка | Создать продукт'

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, files=request.FILES)
        if form.is_valid():
            messages.set_level(request, messages.SUCCESS)
            messages.success(request, 'Новый продукт успешно создан!')
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_products'))
        else:
            messages.error(request, form.errors)
            return HttpResponseRedirect(reverse('admins:admin_products_create'))


class ProductsUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    form_class = ProductsAdminCreateUpdateForm
    success_url = reverse_lazy('admins:admin_products')
    title = 'Админка | Редактирование продукта'


class ProductsActivateView(DeleteView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    success_url = reverse_lazy('admins:admin_products')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active == False:
            self.object.is_active = True
            self.object.save()
            return HttpResponseRedirect(self.get_success_url())
        return HttpResponseRedirect(self.get_success_url())


class ProductsDeleteView(DeleteView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    success_url = reverse_lazy('admins:admin_products')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
