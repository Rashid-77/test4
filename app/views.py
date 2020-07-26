from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .models import Product, SupplierProduct, ProductImages


def index(request):
    return render(request, 'app/index.html')


def my_product(request):
    my_name = 'Quaker'
    all_product = SupplierProduct.objects.all().order_by('vendor_code')

    my_products = []

    for i in all_product:
        if str(i.supplier_name) == my_name:
            my_products.append(i)

    products = Product.objects.all().order_by('vendor_code')

    return render(request, 'app/my_product.html', {'my_products': my_products, 'products': products})


def suppliers(request):
    my_name = 'Quaker'
    competitors_product = SupplierProduct.objects.all().exclude(supplier_name__name=my_name)
    my_products = SupplierProduct.objects.all().filter(supplier_name__name=my_name).order_by('vendor_code')

    cheaper_products = []
    for my in my_products:
        for competitor in competitors_product:
            if my.vendor_code == competitor.vendor_code and my.product_price >= competitor.product_price:
                cheaper_products.append(competitor)

    products = Product.objects.all().order_by('vendor_code')

    return render(request, 'app/suppliers.html', {'cheaper_products': cheaper_products, 'products': products})


def buyer(request):
    print('hello')
    available_product = SupplierProduct.objects.filter(availability__exact='True')
    available_product = available_product.order_by('vendor_code', 'product_price')
    prod_table = Product.objects.all()

    if request.user.is_authenticated:
        user = request.user
    else:
        user = 'anonim'

    print(user)

    return render(request, 'app/buyer.html', {'available_product': available_product, 'prod_table': prod_table, 'user':user})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('my_product')
    else:
        form = AuthenticationForm()
    print(type(form))
    return render(request, 'login.html', {'form': form})


def get_db_data():
    return 'meal'