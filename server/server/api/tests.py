from django.test import TestCase
from rest_framework.test import APIClient

from decimal import Decimal
from .models import Marker

class MarkerTestCase(TestCase):
    def setUp(self):
        self.factory = APIClient()

    def test_create_marker(self):
        request_body = {'latitude': 1123.45678, 'longitude': -1901.23456, 'altitude': 1789.01234}
    
        actual = self.factory.post('/markers/', request_body, format='json').data
        expected = [{'id': 1, 'latitude': Decimal('1123.45678'), 'longitude': Decimal('-1901.23456'), 'altitude': Decimal('1789.01234')}]

        self.assertEqual(actual, expected)

    def test_get_markers(self):
        # Create marker
        request_body = {'latitude': 123.45678, 'longitude': -901.23456, 'altitude': 789.01234}

        self.factory.post('/markers/', request_body, format='json')

        # Get markers
        actual = self.factory.get('/markers/', format='json').data
        expected = [{'id': 1, 'latitude': Decimal('123.45678'), 'longitude': Decimal('-901.23456'), 'altitude': Decimal('789.01234')}]

        self.assertEqual(actual, expected)

    def test_delete_marker(self):
        # Create marker
        request_body = {'latitude': 123.45678, 'longitude': -901.23456, 'altitude': 789.01234}

        self.factory.post('/markers/', request_body, format='json')

        # Delete marker
        actual = self.factory.delete('/markers/1', format='json').data
        expected = []

        self.assertEqual(actual, expected)

    def test_clear_markers(self):
        # Create marker
        request_body = {'latitude': 123.45678, 'longitude': -901.23456, 'altitude': 789.01234}

        self.factory.post('/markers/', request_body, format='json')

        # Clear markers
        actual = self.factory.delete('/markers/', format='json').data
        expected = []

        self.assertEqual(actual, expected)