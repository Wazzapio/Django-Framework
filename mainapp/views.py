from django.views.generic import DetailView, TemplateView, ListView

from mainapp.mixin import BaseClassContextMixin
from mainapp.models import ProductCategory, Product

from django.conf import settings
from django.core.cache import cache


def get_link_category():
    if settings.LOW_CACHE:
        key = 'link_category'
        link_category = cache.get(key)
        if link_category is None:
            link_category = ProductCategory.objects.all()
            cache.set(key, link_category)
        return link_category
    else:
        return ProductCategory.objects.all()

# Create your views here.

class IndexTemplateView(TemplateView, BaseClassContextMixin):
    template_name = 'mainapp/index.html'
    title = 'geekshop'


class CatalogListView(ListView):
    model = Product
    template_name = 'mainapp/products.html'
    title = 'geekshop | Каталог'
    paginate_by = 3
    # categories = ProductCategory.objects.all()
    categories = get_link_category()

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
