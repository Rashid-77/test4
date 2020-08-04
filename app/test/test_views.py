from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    client = Client()


    def test_buyer_GET(self):
        response = self.client.get(reverse('buyer'))

        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'app/buyer.html')

    def test_my_product_GET(self):

        response = self.client.get(reverse('my_product'))

        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'app/my_product.html')


    def test_suppliers_GET(self):

        response = self.client.get(reverse('suppliers'))

        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'app/suppliers.html')

    def test_index_GET(self):

        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/index.html')

