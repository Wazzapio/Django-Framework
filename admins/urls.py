
from django.urls import path

from admins.views import UserListView, UserCreateView, UserUpdateView, \
    UserDeleteView, UserTemplateView, CategoriesListView, CategoriesCreateView, CategoriesUpdateView, \
    CategoriesDeleteView, ProductsListView, ProductsCreateView, ProductsUpdateView, ProductsDeleteView, \
    CategoriesActivateView, ProductsActivateView, UserActivateView

app_name = 'admins'

urlpatterns = [
    path('', UserTemplateView.as_view(), name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users-update/<int:pk>', UserUpdateView.as_view(), name='admin_users_update'),
    path('users-activate/<int:pk>', UserActivateView.as_view(), name='admin_users_activate'),
    path('users-delete/<int:pk>', UserDeleteView.as_view(), name='admin_users_delete'),
    path('categories/', CategoriesListView.as_view(), name='admin_categories'),
    path('categories-create/', CategoriesCreateView.as_view(), name='admin_categories_create'),
    path('categories-update/<int:pk>', CategoriesUpdateView.as_view(), name='admin_categories_update'),
    path('categories-activate/<int:pk>', CategoriesActivateView.as_view(), name='admin_categories_activate'),
    path('categories-delete/<int:pk>', CategoriesDeleteView.as_view(), name='admin_categories_delete'),
    path('products/', ProductsListView.as_view(), name='admin_products'),
    path('products-create/', ProductsCreateView.as_view(), name='admin_products_create'),
    path('products-update/<int:pk>', ProductsUpdateView.as_view(), name='admin_products_update'),
    path('products-activate/<int:pk>', ProductsActivateView.as_view(), name='admin_products_activate'),
    path('products-delete/<int:pk>', ProductsDeleteView.as_view(), name='admin_products_delete'),
]