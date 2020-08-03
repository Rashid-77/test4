import unittest
from app.models import Product, ProductImages, Supplier, SupplierProduct
from django.test import Client

class MyTestCase(unittest.TestCase):
    def test_correct_supplier_product_created(self):
        self.p = Product.objects.create(name='metall_plate', vendor_code='P6')
        self.assertEqual(str(self.p), 'P6')

        self.s = Supplier.objects.create(name='nonsense', telephone='+198244205', zip_code='234234')
        self.assertEqual(str(self.s), 'nonsense')

        self.sp = SupplierProduct.objects.create(
            supplier_name=self.s,
            vendor_code=self.p,
            product_price=12.7,
            availability=True
        )
        self.assertEqual(str(self.sp), 'nonsense - P6 12.7$, True')



if __name__ == '__main__':
    unittest.main()
