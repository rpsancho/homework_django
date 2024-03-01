from django.views.generic import DetailView, TemplateView
from django.views.generic.list import ListView

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'home'
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/detail_view.html'


class AboutView(TemplateView):
    template_name = 'catalog/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'about'
        return context
    