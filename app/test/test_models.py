from django.test import TestCase
from app.models import Product, ProductImages, Supplier, SupplierProduct


class MyTestCase(TestCase):
    def setUp(self):
        self.p = Product.objects.create(name='metall_plate', vendor_code='P99')
        self.s = Supplier.objects.create(name='qwerty', zip_code='998877')

    def test_is_product_added(self):
        self.assertEqual(self.p.vendor_code, 'P99')
        self.assertEqual(self.p.name, 'metall_plate')

    def test_is_Supplier_added(self):
        self.assertEqual(self.s.name, 'qwerty')
        self.assertEqual(self.s.zip_code, '998877')
