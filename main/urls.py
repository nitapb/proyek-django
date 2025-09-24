from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.show_main, name="show_main"),  # halaman utama
    path("products/create/", views.create_product, name="create_product"),
    path("products/<int:id>/", views.show_product, name="show_product"),
    path("products/all/", views.show_all_products, name="show_all_products"),
    path("products/mine/", views.show_my_products, name="show_my_products"),

    # JSON
    path("api/json/", views.products_json, name="products_json"),
    path("api/json/<int:id>/", views.product_json_by_id, name="product_json_by_id"),

    # XML
    path("api/xml/", views.products_xml, name="products_xml"),
    path("api/xml/<int:id>/", views.product_xml_by_id, name="product_xml_by_id"),

    # Authentication
    path("register/", views.register, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
]