from django.contrib import admin
from django.contrib import messages
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from .models import Product, Image, Supplier, SupplierProduct


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'name', 'main_image')


class ImageAdmin(admin.ModelAdmin):
    list_display = ('path', 'product')


class SupplierProductAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'product', 'product_price', 'availability')

    def delete_last_msg(self, request):
        """
        The only purpose to suppress the "success" message after field validation
        In this case only message queue has one or two messages
        if one then it is only SUCCESS
        if two then my message(ERROR or INFO) and default SUCCESS
        """
        storage = messages.get_messages(request)
        if len(storage._queued_messages) > 1:
            del storage._queued_messages[-1]

    def save_model(self, request, obj, form, change):
        """
        1. Save new product if vendor code is unique for this supplier
        2. User can edit existing SupplierProduct by altering supplier field or product field, so vendor code
            became not unique. Шn this case saving is not allowed
        """
        if not SupplierProduct.objects.filter(supplier__exact=obj.supplier, product__exact=obj.product).exists():
            obj.save()
            return
        elif change:
            # if user didn't change supplier or product fieds, so save
            if SupplierProduct.objects.filter(id=obj.id, supplier_id=obj.supplier, product_id=obj.product):
                obj.save()
                return
        msg_dict = {'name': obj.supplier, 'code': obj.product}
        msg = _('The {name} already has a product with this vendor code "{code}". Try another')
        self.message_user(request, format_html(msg, **msg_dict), level=messages.ERROR)

    def response_post_save_add(self, request, obj):
        """
        Figure out where to redirect after the 'Save' button has been pressed
        when adding a new object.
        """
        self.delete_last_msg(request)
        return self._response_post_save(request, obj)

    def response_post_save_change(self, request, obj):
        """
        Figure out where to redirect after the 'Save' button has been pressed
        when editing an existing object.
        """
        self.delete_last_msg(request)
        return self._response_post_save(request, obj)


admin.site.register(Product, ProductAdmin)
admin.site.register(Supplier)
admin.site.register(SupplierProduct, SupplierProductAdmin)
admin.site.register(Image, ImageAdmin)

