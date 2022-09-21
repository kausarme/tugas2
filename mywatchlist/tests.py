from django.test import TestCase, Client
from django.urls import resolve

class ViewsTest(TestCase):
    def test_exists(self):
        response = Client().get('/mywatchlist/')
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        response = Client().get('/mywatchlist/')
        self.assertTemplateUsed(response, 'watchlist.html')

    def test_exists_html(self):
        response = Client().get('/mywatchlist/html')
        self.assertEqual(response.status_code, 200)

    def test_template_html(self):
        response = Client().get('/mywatchlist/html')
        self.assertTemplateUsed(response, 'watchlist.html')

    def test_exists_html2(self):
        response = Client().get('/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)

    def test_template_html2(self):
        response = Client().get('/mywatchlist/html/')
        self.assertTemplateUsed(response, 'watchlist.html')

    def test_exists_json(self):
        response = Client().get('/mywatchlist/json')
        self.assertEqual(response.status_code, 200)

    def test_exists_xml(self):
        response = Client().get('/mywatchlist/xml')
        self.assertEqual(response.status_code, 200)
