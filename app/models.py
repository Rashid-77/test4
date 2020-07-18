

from django.db import models




class Product (models.Model):
    title = models.CharField('product_name', max_length=50)
    vendor_code = models.CharField('vendor code', max_length= 50)

    def __str__(self):
        return self.title


class ProductImages(models.Model):
    vendor_code = models.CharField('vendor code', max_length= 50)
    image_path = models.TextField('img_path', max_length=200)
    # image_path = models.FilePathField()

    def __str__(self):
        return (self.vendor_code, self.image_path)


class Providers(models.Model):
    vendor_code = models.CharField('vendor code', max_length=50)
    provider = models.CharField('vendor code', max_length= 50)
    price = models.DecimalField('price', max_digits=9, decimal_places=2)
    availability = models.BooleanField(default=False)

    def __str__(self):
        return (self.vendor_code, self.provider, self.price, self.availability)