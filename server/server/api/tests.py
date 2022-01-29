from django.test import TestCase
from rest_framework.test import APIClient

class HelloWorldTestCase(TestCase):
    def setUp(self):
        self.factory = APIClient()

    def test_get_hello_world(self):
        actual = self.factory.get('/helloworld/', format='json').data
        expected = {'message': 'Hello World!'}

        self.assertEqual(actual, expected)