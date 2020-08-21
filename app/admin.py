from django.contrib import admin
from django.contrib import messages
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from .models import Product, Image, Supplier



class ImageAdmin(admin.ModelAdmin):
    list_display = ('path', 'order')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'vendor_id', 'supplier', 'price', 'availability', 'main_image')


admin.site.register(Product, ProductAdmin)
admin.site.register(Supplier)
admin.site.register(Image, ImageAdmin)
