from django.urls import path

from blog import views
from blog.apps import BlogConfig

app_name = BlogConfig.name


urlpatterns = [
    path('', views.BlogListView.as_view(), name='list'),
    path('create/', views.BlogCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.BlogUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.BlogDeleteView.as_view(), name='delete'),
    path('view/<int:pk>/', views.BlogDetailView.as_view(), name='view'),
]
