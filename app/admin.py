from django.contrib import admin
from .models import Product, ProductImages, Providers


admin.site.register(Product)
admin.site.register(Providers)
admin.site.register(ProductImages)