from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from .models import Product
from .forms import ProductForm

def show_main(request):
    products = Product.objects.all()
    context = {
        "app_name": "Football Shop",
        "student_name": "Nita Pasaribu",
        "student_class": "PBP A",
        "products": products,
    }
    return render(request, "main.html", context)

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
            return redirect("main:show_main")
    else:
        form = ProductForm()
    return render(request, "create_product.html", {"form": form})

# JSON untuk semua produk
def products_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# JSON untuk produk berdasarkan ID
def product_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# XML untuk semua produk
def products_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# XML untuk produk berdasarkan ID
def product_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")