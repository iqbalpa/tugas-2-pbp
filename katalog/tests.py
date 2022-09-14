from django.test import TestCase, Client
from django.urls import resolve
from .views import show_katalog

# Create your tests here.
class URLTest(TestCase):
    def test_url_katalog(self):
        response = Client().get('/katalog/')
        self.assertEqual(response.status_code, 200)
    def test_template_katalog(self):
        response = Client().get('/katalog/')
        self.assertTemplateUsed(response, 'katalog.html')