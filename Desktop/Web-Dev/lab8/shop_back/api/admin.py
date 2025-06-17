from django.contrib import admin
from .models import Product, Category

# Проверка и отмена регистрации перед повторной регистрацией
if admin.site.is_registered(Product):
    admin.site.unregister(Product)

if admin.site.is_registered(Category):
    admin.site.unregister(Category)

admin.site.register(Product)
admin.site.register(Category)
