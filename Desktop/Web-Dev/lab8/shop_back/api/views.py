from rest_framework import generics
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from django.http import JsonResponse
from rest_framework import generics

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def home(request):
    return JsonResponse({'message': 'Welcome to the Shop API'})

# Список всех продуктов и создание нового продукта
class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Получить, обновить или удалить один продукт
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Список всех категорий и создание новой категории
class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Получить, обновить или удалить одну категорию
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Список продуктов в определённой категории
class CategoryProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs['id']
        return Product.objects.filter(category_id=category_id)
