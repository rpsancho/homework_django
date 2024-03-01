from django.urls import path

from catalog import views


app_name = "catalog"


urlpatterns = [
    path('', views.ProductListView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='detail'),
]
