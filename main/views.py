import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import Product
from .forms import ProductForm
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string

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

@login_required
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            return redirect('main:show_main')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ProductForm(instance=product)
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            html = render_to_string('main/partials/edit_form.html', {'form': form}, request)
            return HttpResponse(html)
    return render(request, 'main/edit_product.html', {'form': form, 'product': product})

@login_required(login_url='main:login')
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)
    if request.method == "POST":
        product.delete()
        messages.success(request, f"Product '{product.name}' berhasil dihapus.")
        return redirect("main:show_my_products")

    return render(request, "delete_product.html", {"product": product})

@csrf_exempt
def delete_product_ajax(request, id):
    if request.method == 'POST':
        try:
            product = Product.objects.get(pk=id)
            product.delete()
            return JsonResponse({'status': 'success', 'message': 'Produk berhasil dihapus!'})
        except Product.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Produk tidak ditemukan.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})

# JSON dan XML endpoints
def products_json(request):
    products = Product.objects.all().order_by('-created_at')
    data = []
    for p in products:
        # dapatkan thumbnail sebagai URL string (atau kosong jika tidak ada)
        thumbnail_url = ""
        try:
            if p.thumbnail and hasattr(p.thumbnail, 'url'):
                thumbnail_url = p.thumbnail.url
        except Exception:
            thumbnail_url = ""

        data.append({
            "id": p.id,
            "name": p.name,
            "price": p.price,
            "thumbnail": thumbnail_url,
            "description": p.description,
            "category": p.category,
            "category_display": p.get_category_display(),
            "user_id": p.user.id if p.user else None,
            "user_username": p.user.username if p.user else None,
            "stock": p.stock,
            "created_at": p.created_at.isoformat() if p.created_at else None,
        })
    return JsonResponse(data, safe=False)

def product_json_by_id(request, id):
    p = get_object_or_404(Product, pk=id)
    thumbnail_url = ""
    try:
        if p.thumbnail and hasattr(p.thumbnail, 'url'):
            thumbnail_url = p.thumbnail.url
    except Exception:
        thumbnail_url = ""
    data = {
        "id": p.id,
        "name": p.name,
        "price": p.price,
        "thumbnail": thumbnail_url,
        "description": p.description,
        "category": p.category,
        "category_display": p.get_category_display(),
        "user_id": p.user.id if p.user else None,
        "user_username": p.user.username if p.user else None,
        "stock": p.stock,
        "created_at": p.created_at.isoformat() if p.created_at else None,
    }
    return JsonResponse(data)

def products_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def product_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")