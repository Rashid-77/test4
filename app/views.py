from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import Product, SupplierProduct, ProductImages
from django.db.models import Q


def user_dispather(request):
    '''
    User dispatcher
    '''
    if not request.user.is_authenticated:
        return render(request, 'app/index.html')
    elif request.user.is_staff:
        return HttpResponseRedirect(reverse('admin:index'))

    user = request.user
    if user.groups.filter(name='Suppliers').exists():
        return my_product(request)
    elif user.groups.filter(name='Buyers').exists():
        return buyer(request)
    else:
        raise Exception('New group have been added but not processed!')
    return render(request, 'app/index.html')


def get_main_thumb_images():
    '''
    this are using to make a table for buyers
    '''
    img_table = ProductImages.objects.filter(
        Q(image_path__endswith='-1.jpg') \
        | Q(image_path__endswith='-1.jpeg') \
        | Q(image_path__endswith='-1.png')
    )
    return img_table


@login_required
def my_product(request):
    '''
    This view makes a table of all products of currently logged in supplier user
    '''
    user = request.user
    if user.groups.filter(name='Suppliers').exists():
        my_products = SupplierProduct.objects.all().filter(supplier__name=user).order_by('product'). \
            values('product__name', 'product__product', 'product_price', 'availability')
        img_table = get_main_thumb_images()
        dataset = {'my_products': my_products, 'img_table': img_table}
        return render(request, 'app/my_product.html', dataset)
    else:
        return HttpResponseNotFound('<h1>Forbidden.</h1><p>You don`t have permission to access</p>')


@login_required
def suppliers(request):
    '''
    This view func makes a table of cheaper available products then products of currently logged in supplier user
    '''
    user = request.user
    if user.groups.filter(name='Suppliers').exists():
        competitors_product = SupplierProduct.objects.all().filter(availability__exact='True'). \
                                                            exclude(supplier__name=user)
        my_products = SupplierProduct.objects.all().filter(supplier__name=user).order_by('product')

        cheaper_products = []
        for my in my_products:
            for competitor in competitors_product:
                if my.product == competitor.product and my.product_price >= competitor.product_price:
                    cheaper_products.append(competitor)

        products = Product.objects.all().order_by('product')
        return render(request, 'app/suppliers.html', {'cheaper_products': cheaper_products, 'products': products})
    else:
        return HttpResponseNotFound('<h1>Forbidden.</h1><p>You don`t have permission to access</p>')


@login_required
def buyer(request):
    '''
    this view func make a table of all available product that provides by suppliers
    '''
    user = request.user
    if user.groups.filter(name='Buyers').exists():
        img_table = get_main_thumb_images()
        available_product = SupplierProduct.objects.filter(availability__exact='True').\
            order_by('product', 'product_price').\
            values('product__name', 'product__product', 'product_price', 'supplier__name')
        dataset = {'available_product': available_product, 'img_table': img_table}
        return render(request, 'app/buyer.html', dataset)
    else:
        return HttpResponseNotFound('<h1>Forbidden.</h1><p>You don`t have permission to access</p>')
