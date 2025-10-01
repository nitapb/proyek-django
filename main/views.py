import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import Product
from .forms import ProductForm

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Akun berhasil dibuat! Silakan login.")
            return redirect("main:login")
    context = {"form": form}
    return render(request, "register.html", context)

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie("last_login", str(datetime.datetime.now()))
            return response
        else:
            messages.error(request, "Username atau Password salah!")
    else:
        form = AuthenticationForm(request)
    return render(request, "login.html", {"form": form})

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse("main:login"))
    response.delete_cookie("last_login")
    return response

@login_required(login_url='main:login')
def show_main(request):
    products = Product.objects.filter(user=request.user)  # default My Products
    context = {
        "app_name": "Football Shop",
        "student_name": "Nita Pasaribu",  # identitas pembuat web
        "student_class": "PBP A",
        "username": request.user.username,
        "last_login": request.COOKIES.get("last_login", "Never"),
        "products": products,
        "view": "mine",   # supaya tombol toggle tahu posisi default
    }
    return render(request, "main.html", context)

@login_required(login_url='main:login')
def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect("main:show_main")
    else:
        form = ProductForm()
    return render(request, "create_product.html", {"form": form})

@login_required(login_url='main:login')
def show_all_products(request):
    products = Product.objects.all()
    context = {
        "app_name": "Football Shop",
        "student_name": "Nita Pasaribu",
        "student_class": "PBP A",
        "username": request.user.username,
        "last_login": request.COOKIES.get("last_login", "Never"),
        "products": products,
        "view": "all",
    }
    return render(request, "main.html", context)

@login_required(login_url='main:login')
def show_my_products(request):
    products = Product.objects.filter(user=request.user)
    context = {
        "app_name": "Football Shop",
        "student_name": "Nita Pasaribu",
        "student_class": "PBP A",
        "username": request.user.username,
        "last_login": request.COOKIES.get("last_login", "Never"),
        "products": products,
        "view": "mine",
    }
    return render(request, "main.html", context)

@login_required(login_url='main:login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {
        "product": product,
    }
    return render(request, "product_detail.html", context)

@login_required(login_url='main:login')
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f"Product '{product.name}' berhasil diperbarui.")
            return redirect("main:show_my_products")
    else:
        form = ProductForm(instance=product)

    return render(request, "edit_product.html", {"form": form, "product": product})

@login_required(login_url='main:login')
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)
    if request.method == "POST":
        product.delete()
        messages.success(request, f"Product '{product.name}' berhasil dihapus.")
        return redirect("main:show_my_products")

    return render(request, "delete_product.html", {"product": product})

# JSON dan XML endpoints
def products_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def product_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def products_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def product_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")