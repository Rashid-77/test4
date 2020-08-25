from django.db import models
# from django.db.models.fields import PositiveIntegerField


class Image(models.Model):
    """
    Here is the other product images.
    """
    path = models.ImageField(default=None, blank=False)

    def __str__(self):
        return '{0} {1}'.format(self.path, self.order)


class Product(models.Model):
    """
    Product description with main image
    """
    name = models.CharField('product name', max_length=50)
    vendor_id = models.CharField('vendor code', default=None, max_length=50)
    supplier = models.ForeignKey('Supplier', default=None, on_delete=models.CASCADE)
    price = models.DecimalField('Price', default=None, max_digits=11, decimal_places=2)
    availability = models.BooleanField(default=False)
    main_image = models.ImageField('Main image', default='no_image_available-1.png', blank=False)
    image = models.ManyToManyField(Image, blank=True, related_name='products', verbose_name='Additional images')

    class Meta:
        unique_together = [['supplier', 'vendor_id']]

    def __str__(self):
        return '{0}'.format(self.name, self.price, self.availability)


class Supplier(models.Model):
    """
    All information about supplier are here
    """
    name = models.CharField('Supplier name', default='', max_length=50)
    # telephone = models.CharField('Telephone', default=None, max_length=12)
    zip_code = models.CharField('zip code', default=None, max_length=6)

    def __str__(self):
        return self.name

