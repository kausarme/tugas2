from django.test import TestCase
from katalog.models import CatalogItem


# Create your tests here.

class CatalogTestCase(TestCase):
    def setUp(self):
        CatalogItem.objects.create(item_name="Bakso",
                                   item_price=10000,
                                   item_stock=10,
                                   description="Bakso Test",
                                   rating=5,
                                   item_url="www.google.com")

    def test_url(self):
        """Url is correct"""
        bakso = CatalogItem.objects.get(item_name="Bakso")
        self.assertEqual(bakso.item_url, "www.google.com")

    def test_item_price(self):
        """Url is correct"""
        bakso = CatalogItem.objects.get(item_name="Bakso")
        self.assertEqual(bakso.item_price, 10000)

    def test_item_stock(self):
        """Url is correct"""
        bakso = CatalogItem.objects.get(item_name="Bakso")
        self.assertEqual(bakso.item_stock, 10)

    def test_description(self):
        """Url is correct"""
        bakso = CatalogItem.objects.get(item_name="Bakso")
        self.assertEqual(bakso.description, "Bakso Test")

    def test_rating(self):
        """Url is correct"""
        bakso = CatalogItem.objects.get(item_name="Bakso")
        self.assertEqual(bakso.rating, 5)