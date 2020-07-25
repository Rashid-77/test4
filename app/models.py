

from django.db import models


class Product(models.Model):
    name = models.CharField('product_name', max_length=50)
    vendor_code = models.CharField('vendor code', default=None, max_length=50)

    def __str__(self):
        return '{0}'.format(self.vendor_code)
        # return '{0} {1}'.format(self.name, self.vendor_code)


class ProductImages(models.Model):
    vendor_code = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image_path = models.TextField('img_path', max_length=200)
    # image_path = models.FilePathField()

    def __str__(self):
        return '({0}) {1}'.format(self.vendor_code, self.image_path)


class Supplier(models.Model):
    name = models.CharField('Provider name', default='', max_length=50)
    telephone = models.CharField('Telephone', default=None, max_length=12)
    zip_code = models.CharField('zip code', default=None, max_length=6)

    def __str__(self):
        return '{0}'.format(self.name)

    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'


class SupplierProduct(models.Model):
    supplier_name = models.ForeignKey(Supplier, default=None, on_delete=models.CASCADE)
    vendor_code = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    product_price = models.DecimalField('Price', default=None, max_digits=11, decimal_places=2)
    availability = models.BooleanField(default=False)

    def __str__(self):
        return '{0} - {1} {2}$, {3}'.format(self.supplier_name, self.vendor_code, self.product_price, self.availability)
