from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q, OuterRef, Exists
from django.core.exceptions import PermissionDenied
from .models import Product, Image, Supplier


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
        my_products = Product.objects.filter(supplier__name=user).order_by('vendor_id'). \
            values('name', 'vendor_id', 'price', 'availability', 'main_image')
        dataset = {'my_products': my_products}
        return render(request, 'app/my_product.html', dataset)
    else:
        raise PermissionDenied


@login_required
def suppliers(request):
    '''
    This view func makes a table of cheaper available products then products of currently logged in supplier user
    '''
    user = request.user
    if user.groups.filter(name='Suppliers').exists():
        cheaper_products = Product.objects.annotate(
            exist=Exists(Product.objects.filter(
                Q(supplier__name=user),
                ~Q(supplier_id=OuterRef('supplier_id')),
                vendor_id=OuterRef('vendor_id'),
                price__gt= OuterRef('price')
                )
            )
        ).filter(availability=True, exist=True).values('name', 'vendor_id', 'supplier__name', 'price')
        dataset = {'cheaper_products': cheaper_products}
        return render(request, 'app/suppliers.html', {'cheaper_products': cheaper_products})
    else:
        raise PermissionDenied


@login_required
def buyer(request):
    '''
    this view func make a table of all available product that provides by suppliers
    '''
    user = request.user
    if user.groups.filter(name='Buyers').exists():
        available_product = Product.objects.filter(availability__exact='True'). \
            order_by('vendor_id', 'price'). \
            values('id', 'name', 'vendor_id', 'supplier__name', 'price', 'main_image')
        dataset = {'available_product': available_product}
        return render(request, 'app/buyer.html', dataset)
    else:
         raise PermissionDenied