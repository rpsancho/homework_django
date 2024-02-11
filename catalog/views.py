from django.shortcuts import render


# Create your views here.
def index(reqest):
    context = {
        'title': 'home',
    }
    return render(reqest, 'catalog/index.html', context=context)


def about(reqest):
    context = {
        'title': 'about',
    }
    return render(reqest, 'catalog/about.html', context=context)
