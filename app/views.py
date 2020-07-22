from django.shortcuts import render
# from django.contrib.auth import models.user
from django.http import HttpResponse
from .models import Product, Providers,ProductImages


def index(request):
    return render(request, 'app/index.html')


def provider(request):
    # aqq = Providers.objects.filter(provider__contains='Vas')
    aqq = Providers.objects.all().order_by('provider')
    prod_table = Product.objects.all()
    # print(aqq)
    # print(type(aqq))
    # print(prod_table)
    # print(type(prod_table))
    # cnt = 0
    # for i in aqq:
    #     print('i=', cnt, i.vendor_code)
    #     cnt += 1
    #     z = 0
    #     for j in prod_table:
    #         print('z=', z, j)
    #         z += 1
    #         if j == i.vendor_code:
    #             print('{0}, {1}'.format(j.vendor_code, j.name))
    #             break

    return render(request, 'app/provider.html', {'prov_table': aqq, 'prod_table': prod_table})


def buyer(request):
    available_product = Providers.objects.filter(availability__exact='True')
    available_product = available_product.order_by('vendor_code', 'price')
    prod_table = Product.objects.all()

    if request.user.is_authenticated:
        user = request.user
        groups = request.user.groups
    else:
        user = 'anonim'
        groups = 'no group ?'
    print(user)
    print(groups)
    # available_product = available_product.filter(provider__contains='Boris')
    # if available_product:
    #     print('yes')
    # else:
    #     print(('no'))
    # for i in available_product:
    #     print(i.vendor_code, i.price, i.provider, i.availability)
    return render(request, 'app/buyer.html', {'available_product': available_product, 'prod_table': prod_table, 'user':user})


def login(request):
    return render(request, 'app/login.html')


def get_db_data():
    return 'meal'