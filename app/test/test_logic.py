from django.test import TestCase
from app.models import Product, Image, Supplier
from django.contrib.auth.models import User, Group
from django.test import Client
from django.urls import reverse


class TestLogic(TestCase):
    c = Client()

    def setUp(self):
        self.user0 = User.objects.create_user('buyer_1', 'Malcona@mail.com', 'la*cgw!3_M')
        # self.user0.save()

        self.user1 = User.objects.create_user('Malcona', 'Malcona@mail.com', 'II_73fs9#')
        # self.user1.save()

        self.user2 = User.objects.create_user('TractorCo', 'TractorCo@mail.com', 'WWQ7fs9#')
        # self.user2.save()

        self.user3 = User.objects.create_user('Zanzix', 'Zanzix@mail.com', 'TR_973fs9#')
        # self.user3.save()

        self.g1 = Group.objects.create(name='Buyers')
        self.g1.user_set.add(self.user0)

        self.g1 = Group.objects.create(name='Suppliers')
        self.g1.user_set.add(self.user1, self.user2, self.user3)

        self.s1 = Supplier.objects.create(name='Malcona', zip_code='652984')
        self.p1 = Product.objects.create(name='Fish', vendor_id='P1', availability=True, supplier=self.s1, price=3)
        self.p2 = Product.objects.create(name='Cabbage', vendor_id='P2', availability=True, supplier=self.s1, price=19)
        self.p3 = Product.objects.create(name='Iron', vendor_id='P3', availability=True, supplier=self.s1, price=95)
        self.s1.save()
        self.p1.save()
        self.p2.save()
        self.p3.save()

        self.s2 = Supplier.objects.create(name='TractorCo', zip_code='411024')
        self.p1 = Product.objects.create(name='Fish', vendor_id='P1', availability=True, supplier=self.s2, price=8)
        self.p2 = Product.objects.create(name='Cabbage', vendor_id='P2', availability=True, supplier=self.s2, price=18)
        self.p3 = Product.objects.create(name='Iron', vendor_id='P3', availability=False, supplier=self.s2, price=94)
        self.s2.save()
        self.p1.save()
        self.p2.save()

        self.s3 = Supplier.objects.create(name='Zanzix', zip_code='411024')
        self.p1 = Product.objects.create(name='Fish', vendor_id='P1', availability=False, supplier=self.s3, price=12)
        self.p2 = Product.objects.create(name='Cabbage', vendor_id='P2', availability=True, supplier=self.s3, price=17)
        self.p3 = Product.objects.create(name='Iron', vendor_id='P3', availability=True, supplier=self.s3, price=89)
        self.s3.save()
        self.p2.save()
        self.p3.save()

    def test_is_buyer(self):
        self.g1.user_set.add(self.user0)

        a = self.c.login(username='buyer_1', password='la*cgw!3_M')

        response = self.c.get(reverse('buyer'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['available_product']), 7)

        self.assertEqual(response.context['available_product'][0]['vendor_id'], 'P1')
        self.assertEqual(response.context['available_product'][1]['vendor_id'], 'P1')
        self.assertEqual(response.context['available_product'][2]['vendor_id'], 'P2')
        self.assertEqual(response.context['available_product'][3]['vendor_id'], 'P2')
        self.assertEqual(response.context['available_product'][4]['vendor_id'], 'P2')
        self.assertEqual(response.context['available_product'][5]['vendor_id'], 'P3')
        self.assertEqual(response.context['available_product'][6]['vendor_id'], 'P3')

        self.assertEqual(response.context['available_product'][0]['price'], 3)
        self.assertEqual(response.context['available_product'][1]['price'], 8)
        self.assertEqual(response.context['available_product'][2]['price'], 17)
        self.assertEqual(response.context['available_product'][3]['price'], 18)
        self.assertEqual(response.context['available_product'][4]['price'], 19)
        self.assertEqual(response.context['available_product'][5]['price'], 89)
        self.assertEqual(response.context['available_product'][6]['price'], 95)
        self.c.logout()

    def test_is_login_my_product(self):
        a = self.c.login(username='Malcona', password='II_73fs9#')
        response = self.c.get(reverse('my_product'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['my_products'][0]['vendor_id'], 'P1')
        self.assertEqual(response.context['my_products'][1]['vendor_id'], 'P2')
        self.assertEqual(response.context['my_products'][2]['vendor_id'], 'P3')

        self.assertEqual(response.context['my_products'][0]['price'], 3)
        self.assertEqual(response.context['my_products'][1]['price'], 19)
        self.assertEqual(response.context['my_products'][2]['price'], 95)

    def test_is_login_supplier(self):
        a = self.c.login(username='Malcona', password='II_73fs9#')

        response = self.c.get(reverse('suppliers'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['cheaper_products']), 3)

        self.assertEqual(response.context['cheaper_products'][0]['vendor_id'], 'P2')
        self.assertEqual(response.context['cheaper_products'][1]['vendor_id'], 'P2')
        self.assertEqual(response.context['cheaper_products'][2]['vendor_id'], 'P3')

        self.assertEqual(response.context['cheaper_products'][0]['price'], 18)
        self.assertEqual(response.context['cheaper_products'][1]['price'], 17)
        self.assertEqual(response.context['cheaper_products'][2]['price'], 89)

        self.c.logout()
