from django.shortcuts import render

from catalog.models import Product


# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {
        'title': 'home',
        'object_list': products,
    }
    return render(request, 'catalog/index.html', context=context)


def detail_view(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'object': product,
    }
    return render(request, 'catalog/detail_view.html', context=context)


def about(request):
    context = {
        'title': 'about',
    }
    return render(request, 'catalog/about.html', context=context)
