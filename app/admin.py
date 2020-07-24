from django.contrib import admin
from .models import Product, ProductImages, Providers, ProviderProduct


admin.site.register(Product)
admin.site.register(Providers)
admin.site.register(ProductImages)
admin.site.register(ProviderProduct)