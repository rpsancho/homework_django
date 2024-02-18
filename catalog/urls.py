from django.urls import path

from catalog import views


app_name = "catalog"

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('products/<int:pk>/', views.detail_view, name='detail'),
]
