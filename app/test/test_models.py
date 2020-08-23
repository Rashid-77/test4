from django.test import TestCase
from app.models import Product, Image, Supplier


class MyTestCase(TestCase):

    def setUp(self):
        self.s = Supplier.objects.create(name='qwerty', zip_code='998877')
        self.p = Product.objects.create(name='metall_plate', vendor_id='P99', supplier=self.s,\
                                        price=3.9)

    def test_is_product_added(self):
        self.assertEqual(self.p.vendor_id, 'P99')
        self.assertEqual(self.p.name, 'metall_plate')
        self.assertEqual(self.p.main_image, 'no_image_available-1.png')

    def test_is_Supplier_added(self):
        self.assertEqual(self.s.name, 'qwerty')
        self.assertEqual(self.s.zip_code, '998877')
