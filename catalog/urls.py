from django.urls import path

from catalog import views


app_name = "catalog"

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
