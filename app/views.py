from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Providers,ProductImages


def index(request):
    return render(request, 'app/index.html')


def provider(request):
    aqq = Providers.objects.filter(provider__contains='Misha')
    return render(request, 'app/provider.html', {'prov_table': aqq})


def buyer(request):
    # available_product = Providers.objects.filter(availability__contains='True')
    available_product = Providers.objects.order_by('vendor_code')
    for i in available_product:
        print(i.vendor_code, i.price, i.provider)
    return render(request, 'app/buyer.html', {'prod_table': available_product})


def login(request):
    return render(request, 'app/login.html')


def get_db_data():
    return 'meal'