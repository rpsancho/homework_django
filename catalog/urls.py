from django.urls import path
from catalog.apps import CatalogConfig

from catalog import views


app_name = CatalogConfig.name


urlpatterns = [
    path('', views.ProductListView.as_view(), name='index'),
    path('product/create/', views.ProductCreateView.as_view(), name='create'),
    path('product/update/<int:pk>/', views.ProductUpdateView.as_view(), name='update'),
    path('product/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='delete'),
    path('product/view/<int:pk>/', views.ProductDetailView.as_view(), name='view'),
    path('about/', views.AboutView.as_view(), name='about'),
]
