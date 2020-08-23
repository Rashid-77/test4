from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app.views import user_dispather, my_product, suppliers, buyer


class TestUrls(SimpleTestCase):

    def test_buyer_url_is_resolved(self):
        url = reverse('buyer')
        self.assertEqual(resolve(url).func, buyer)

    def test_my_product_url_is_resolved(self):
        url = reverse('my_product')
        self.assertEqual(resolve(url).func, my_product)

    def test_suppliers_url_is_resolved(self):
        url = reverse('suppliers')
        self.assertEqual(resolve(url).func, suppliers)

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, user_dispather)
