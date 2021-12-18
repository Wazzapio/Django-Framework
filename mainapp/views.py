from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import DetailView, TemplateView, ListView

from mainapp.mixin import BaseClassContextMixin, UserDispatchMixin
from mainapp.models import ProductCategory, Product


# Create your views here.


class IndexTemplateView(TemplateView, BaseClassContextMixin):
    template_name = 'mainapp/index.html'
    title = 'geekshop'


class CatalogListView(ListView):
    model = Product
    template_name = 'mainapp/products.html'
    title = 'geekshop | Каталог'
    paginate_by = 3
    categories = ProductCategory.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CatalogListView, self).get_context_data(**kwargs)
        context['title'] = self.title
        context['categories'] = self.categories
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'mainapp/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        product = self.get_object()
        context['product'] = product
        return context
