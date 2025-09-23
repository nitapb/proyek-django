from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.show_main, name="show_main"),  # halaman utama
    path("products/", views.show_products, name="show_products"),
    path("products/create/", views.create_product, name="create_product"),
    path("products/<int:id>/", views.show_product, name="show_product"),

    # JSON
    path("api/json/", views.products_json, name="products_json"),
    path("api/json/<int:id>/", views.product_json_by_id, name="product_json_by_id"),

    # XML
    path("api/xml/", views.products_xml, name="products_xml"),
    path("api/xml/<int:id>/", views.product_xml_by_id, name="product_xml_by_id"),
]