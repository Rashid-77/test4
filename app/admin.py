from django.contrib import admin
from .models import Product, ProductImages, Supplier, SupplierProduct


admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(ProductImages)
admin.site.register(SupplierProduct)
