from django.contrib import admin
from django.contrib import messages
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from .models import Product, ProductImages, Supplier, SupplierProduct


class ProductAdmin(admin.ModelAdmin):
    list_display = ('vendor_code', 'name')


class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ('vendor_code', 'image_path')


class SupplierProductAdmin(admin.ModelAdmin):
    list_display = ('supplier_name', 'vendor_code', 'product_price', 'availability')

    def delete_last_msg(self, request):
        '''
        The only purpose to suppress the "success" message after field validation
        In this case only message queue has one or two messages
        if one then it is only SUCCESS
        if two then my message(ERROR or INFO) and default SUCCESS
        '''
        storage = messages.get_messages(request)
        if len(storage._queued_messages) > 1:
            del storage._queued_messages[-1]

    def is_vendor_code_unique(self, obj):
        '''
        For new and editing existing SupplierProduct
        '''
        this_suppliers_products = SupplierProduct.objects.filter(supplier_name__exact=obj.supplier_name)
        for sp in this_suppliers_products:
            if sp.vendor_code == obj.vendor_code:
                return False
        return True

    def save_model(self, request, obj, form, change):
        '''
        Save new product(price) for this supplier if vendor code is unique for this supplier
        '''
        msg_dict = {
            'name': obj.supplier_name,
            'code': obj.vendor_code,
        }
        if self.is_vendor_code_unique(obj):
            obj.save()
        elif not change:
            msg = _('The {name} already has a product with this vendor code "{code}". Try another')
            self.message_user(request, format_html(msg, **msg_dict), level=messages.ERROR)
        else:
            old = SupplierProduct.objects.get(pk=obj.id)
            if old.supplier_name != obj.supplier_name or old.vendor_code != obj.vendor_code:
                msg = _('The {name} already has a product with this vendor code "{code}". Try another')
                self.message_user(request, format_html(msg, **msg_dict), level=messages.ERROR)
            elif old.product_price == obj.product_price:
                # don`t save to database, save time consumption
                self.message_user(request, _('Nothing have been changed'), level=messages.INFO)
            else:
                obj.save()

    def response_post_save_add(self, request, obj):
        """
        Figure out where to redirect after the 'Save' button has been pressed
        when adding a new object.
        """
        print('response_post_save_add----------')
        self.delete_last_msg(request)
        return self._response_post_save(request, obj)

    def response_post_save_change(self, request, obj):
        """
        Figure out where to redirect after the 'Save' button has been pressed
        when editing an existing object.
        """
        print('response_post_save_change----------')
        self.delete_last_msg(request)
        return self._response_post_save(request, obj)


admin.site.register(Product, ProductAdmin)
admin.site.register(Supplier)
admin.site.register(ProductImages, ProductImagesAdmin)
admin.site.register(SupplierProduct, SupplierProductAdmin)

