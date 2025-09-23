from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category", "is_available", "stock", "created_at")
    list_filter = ("category", "is_available", "created_at")
    search_fields = ("name", "description")