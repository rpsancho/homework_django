from django.urls import reverse
from django.views.generic import CreateView, DeleteView, DetailView, TemplateView, UpdateView
from django.views.generic.list import ListView
from catalog.forms import ProductCreateForm

from catalog.models import Product, Version


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'catalog/product_form.html'
    success_url = ''


class ProductListView(ListView):
    model = Version
    template_name = 'catalog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Product.objects.filter(version__is_current_version=True)
        for item in context['object_list']:
            item.version_number = Version.objects.get(product_id=item.pk, is_current_version=True).version_number
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'catalog/product_form.html'
    # fields = '__all__'
    # exclude = ('created_at', 'updated_at',)
    # success_url = '/product/'

    def get_success_url(self):
        return reverse('catalog:view', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = ''


class AboutView(TemplateView):
    template_name = 'catalog/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'about'
        return context
    