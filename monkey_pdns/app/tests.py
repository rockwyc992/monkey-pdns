from django.test import TestCase
from django.urls import reverse

from .views import hello

class View_hello_tests(TestCase):

    def test_hello(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello, world.')

