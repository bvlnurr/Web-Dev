from django.urls import path
from .views import ProductListView
from . import views
from .views import (
    ProductListView, ProductDetailView,
    CategoryListView, CategoryDetailView,
    CategoryProductListView
)

urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('categories/<int:id>/products/', views.CategoryProductListView.as_view(), name='category-product-list'),
]

