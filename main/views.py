from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Product
from .forms import ProductForm

# Halaman daftar produk
def show_products(request):
    products = Product.objects.all()
    return render(request, "product_list.html", {"products": products})

# Halaman detail produk
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "product_detail.html", {"product": product})

# Form untuk tambah produk
def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main:show_products")
    else:
        form = ProductForm()
    return render(request, "create_product.html", {"form": form})

# JSON untuk semua produk
def products_json(request):
    products = list(Product.objects.values())
    return JsonResponse(products, safe=False)

# JSON untuk produk berdasarkan ID
def product_json_by_id(request, id):
    product = get_object_or_404(Product, pk=id)
    return JsonResponse({
        "id": product.id,
        "name": product.name,
        "price": product.price,
        "description": product.description,
        "thumbnail": product.thumbnail,
        "category": product.category,
        "is_featured": product.is_featured,
        "stock": product.stock,
        "created_at": product.created_at,
    })