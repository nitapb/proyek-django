from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.show_products, name='show_products'),      # daftar produk (root)
    path('products/', views.show_products, name='show_products_alt'),
    path('products/create/', views.create_product, name='create_product'),
    path('products/<int:id>/', views.show_product, name='show_product'),

    # endpoints data delivery JSON
    path('api/json/', views.products_json, name='products_json'),
    path('api/json/<int:id>/', views.product_json_by_id, name='product_json_by_id'),
]