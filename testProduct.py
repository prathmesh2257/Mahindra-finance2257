from django.test import TestCase
from  .models import Product


class ProductTestCase(TestCase):
    def testProduct(self):
        product = Product(name="My test product", price=20000)
        self.assertEqual(product.name, "My test product")
        self.assertEqual(product.price, 20000)