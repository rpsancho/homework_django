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
    path('versions/', views.VersionListView.as_view(), name='list_ver'),
    path('version/create/', views.VersionCreateView.as_view(), name='create_ver'),
    path('version/update/<int:pk>/', views.VersionUpdateView.as_view(), name='update_ver'),
    path('version/delete/<int:pk>/', views.VersionDeleteView.as_view(), name='delete_ver'),
    path('about/', views.AboutView.as_view(), name='about'),
]
