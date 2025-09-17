from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core import serializers
from .models import Product
from .forms import ProductForm

# halaman daftar produk
def show_products(request):
    products = Product.objects.all()
    return render(request, "product_list.html", {"products": products})

# halaman detail produk
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "product_detail.html", {"product": product})

# halaman form tambah produk
def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main:show_products")
    else:
        form = ProductForm()
    return render(request, "create_product.html", {"form": form})

# JSON: semua produk
def products_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# JSON: produk by ID
def product_json_by_id(request, id):
    product = get_object_or_404(Product, pk=id)
    return HttpResponse(serializers.serialize("json", [product]), content_type="application/json")