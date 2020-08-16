from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q, OuterRef, Exists
from django.db import connection
from .models import Product, SupplierProduct, Image, Supplier


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


@login_required
def my_product(request):
    '''
    This view makes a table of all products of currently logged in supplier user
    '''
    user = request.user
    if user.groups.filter(name='Suppliers').exists():
        my_products = SupplierProduct.objects.\
            filter(supplier__name=user).order_by('product'). \
            values('product__name', 'product__product', 'product_price', 'availability', 'product__main_image')
        dataset = {'my_products': my_products}
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
        cheaper_products = SupplierProduct.objects.annotate(
            exist=Exists(SupplierProduct.objects.filter(
                Q(supplier__name=user),
                ~Q(supplier_id=OuterRef('supplier_id')),
                availability=True,
                product_id=OuterRef('product_id'),
                product_price__gt = OuterRef('product_price')
                )
            )
        ).filter(availability=True, exist=True).order_by('product', 'product_price'). \
            values('product__name', 'product__product', 'supplier__name', 'product_price')
        return render(request, 'app/suppliers.html', {'cheaper_products': cheaper_products})
    else:
        return HttpResponseNotFound('<h1>Forbidden.</h1><p>You don`t have permission to access</p>')


@login_required
def buyer(request):
    '''
    this view func make a table of all available product that provides by suppliers
    '''
    user = request.user
    if user.groups.filter(name='Buyers').exists():
         available_product = SupplierProduct.objects.\
             filter(availability__exact='True').\
            order_by('product', 'product_price').\
            values('product__name', 'product__product', 'product_price', 'supplier__name', 'product__main_image')
         dataset = {'available_product': available_product}
         return render(request, 'app/buyer.html', dataset)
    else:
         return HttpResponseNotFound('<h1>Forbidden.</h1><p>You don`t have permission to access</p>')
