from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [

    path('main/', views.show_main, name='show_main'),
    path('', views.show_products, name='show_products'),
    path('products/', views.show_products, name='show_products_alt'),
    path('products/create/', views.create_product, name='create_product'),
    path('products/<int:id>/', views.show_product, name='show_product'),

    # endpoints data delivery JSON
    path('api/json/', views.products_json, name='products_json'),
    path('api/json/<int:id>/', views.product_json_by_id, name='product_json_by_id'),

    # endpoints data delivery XML
    path('api/xml/', views.products_xml, name='products_xml'),
    path('api/xml/<int:id>/', views.product_xml_by_id, name='product_xml_by_id'),
]