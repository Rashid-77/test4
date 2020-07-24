from django.shortcuts import render
# from django.contrib.auth import models.user
from .models import Product, Providers, ProviderProduct, ProductImages


def index(request):
    return render(request, 'app/index.html')


def my_product(request):
    my_name = 'Itt Telecom'
    all_product = ProviderProduct.objects.all().order_by('vendor_code')

    my_products = []

    for i in all_product:
        if str(i.provider) == my_name:
            my_products.append(i)

    products = Product.objects.all().order_by('vendor_code')

    return render(request, 'app/my_product.html', {'my_products': my_products, 'products': products})


def suppliers(request):
    my_name = 'Itt Telecom'
    all_product = ProviderProduct.objects.all()
    competitors_product = []
    my_products = []
    for i in all_product:
        if str(i.provider) == my_name:
            my_products.append(i)
        elif i.availability:
            competitors_product.append(i)

    cheaper_products = []
    for my in my_products:
        for competitor in competitors_product:
            if my.vendor_code == competitor.vendor_code and my.price >= competitor.price:
                cheaper_products.append(competitor)

    products = Product.objects.all().order_by('vendor_code')

    return render(request, 'app/suppliers.html', {'cheaper_products': cheaper_products, 'products': products})


def buyer(request):
    available_product = ProviderProduct.objects.filter(availability__exact='True')
    available_product = available_product.order_by('vendor_code', 'price')
    prod_table = Product.objects.all()

    if request.user.is_authenticated:
        user = request.user
    else:
        user = 'anonim'

    print(user)

    return render(request, 'app/buyer.html', {'available_product': available_product, 'prod_table': prod_table, 'user':user})


def login(request):
    return render(request, 'app/login.html')


def get_db_data():
    return 'meal'