from django.db import models


class Product(models.Model):
    '''
    here we can add main product image, but better place image to another table,
    where all images will be stored
    '''
    name = models.CharField('product_name', max_length=50)
    vendor_code = models.CharField('vendor code', default=None, max_length=50, unique=True)

    def __str__(self):
        return '{0}'.format(self.vendor_code)


class ProductImages(models.Model):
    '''
    image extension should be jpg, jpeg or png
    '''
    vendor_code = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image_path = models.ImageField(default='no_image_available-1.png', blank=True)

    def __str__(self):
        return '{0}'.format(self.vendor_code)


class Supplier(models.Model):
    '''
    All information about supplier are here
    '''
    name = models.CharField('Provider name', default='', max_length=50)
    # telephone = models.CharField('Telephone', default=None, max_length=12)
    zip_code = models.CharField('zip code', default=None, max_length=6)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'


class SupplierProduct(models.Model):
    supplier_name = models.ForeignKey(Supplier, default=None, on_delete=models.CASCADE)
    vendor_code = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    product_price = models.DecimalField('Price', default=None, max_digits=11, decimal_places=2)
    availability = models.BooleanField(default=False)

    def __str__(self):
        return '{0}'.format(self.supplier_name)


