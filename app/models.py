from django.db import models



class Product(models.Model):
    '''
    Product description with main image
    '''
    name = models.CharField('product name', max_length=50)
    product = models.CharField('vendor code', default=None, max_length=50, unique=True)
    main_image = models.ImageField(default='no_image_available-1.png', blank=True, verbose_name='main image')
    # image = models.ForeignKey(Image, default=None, on_delete=models.SET_DEFAULT, null=True, blank=True, verbose_name='main image')

    def __str__(self):
        return '{0}'.format(self.product, self.name)


class Image(models.Model):
    '''
    Here is the other product images.
    '''
    path = models.ImageField(default='no_image_available-1.png', blank=False)
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return '{0} {1}'.format(self.path, self.product)


class Supplier(models.Model):
    '''
    All information about supplier are here
    '''
    name = models.CharField('Provider name', default='', max_length=50)
    # telephone = models.CharField('Telephone', default=None, max_length=12)
    zip_code = models.CharField('zip code', default=None, max_length=6)

    def __str__(self):
        return self.name


class SupplierProduct(models.Model):
    '''
    Here is information about what products the supplier has and how much they cost
    '''
    supplier = models.ForeignKey(Supplier, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    product_price = models.DecimalField('Price', default=None, max_digits=11, decimal_places=2)
    availability = models.BooleanField(default=False)

    def __str__(self):
        return '{0}'.format(self.supplier)

