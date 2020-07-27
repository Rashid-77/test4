from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound
from .models import Product, SupplierProduct, ProductImages


def index(request):
    if request.user.is_authenticated:
        user = request.user
    else:
        return render(request, 'app/index.html')

    if user.groups.filter(name='Suppliers').exists():
        return my_product(request)
    elif user.groups.filter(name='Buyers').exists():
        return buyer(request)

    return render(request, 'app/index.html')


@login_required
def my_product(request):
    user = request.user
    if user.groups.filter(name='Suppliers').exists():
        all_product = SupplierProduct.objects.all().order_by('vendor_code')
        my_products = []

        for i in all_product:
            if str(i.supplier_name) == str(request.user):
                my_products.append(i)

        products = Product.objects.all().order_by('vendor_code')
        return render(request, 'app/my_product.html', {'my_products': my_products, 'products': products})
    else:
        return HttpResponseNotFound('<h1>Forbidden.</h1><p>You don`t have permission to access</p>')


@login_required
def suppliers(request):
    user = request.user
    if user.groups.filter(name='Suppliers').exists():
        competitors_product = SupplierProduct.objects.all().exclude(supplier_name__name=user)
        my_products = SupplierProduct.objects.all().filter(supplier_name__name=user).order_by('vendor_code')

        cheaper_products = []
        for my in my_products:
            for competitor in competitors_product:
                if my.vendor_code == competitor.vendor_code and my.product_price >= competitor.product_price:
                    cheaper_products.append(competitor)

        products = Product.objects.all().order_by('vendor_code')
        return render(request, 'app/suppliers.html', {'cheaper_products': cheaper_products, 'products': products})
    else:
        return HttpResponseNotFound('<h1>Forbidden.</h1><p>You don`t have permission to access</p>')


@login_required
def buyer(request):
    user = request.user
    if user.groups.filter(name='Buyers').exists():
        available_product = SupplierProduct.objects.filter(availability__exact='True')
        available_product = available_product.order_by('vendor_code', 'product_price')
        prod_table = Product.objects.all()
        return render(request, 'app/buyer.html', {'available_product': available_product, 'prod_table': prod_table})
    else:
        return HttpResponseNotFound('<h1>Forbidden.</h1><p>You don`t have permission to access</p>')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


