from django.test import TestCase
from rest_framework.test import APIClient

from decimal import Decimal

from .models import Marker

class MarkerTestCase(TestCase):
    def test_create_marker(self):
        factory = APIClient()
        request_body = {'latitude': 1123.45678, 'longitude': -1901.23456, 'altitude': 1789.01234}
    
        actual = factory.post('/markers/', request_body, format='json').data
        expected = [{'id': 1, 'latitude': Decimal('1123.45678'), 'longitude': Decimal('-1901.23456'), 'altitude': Decimal('1789.01234')}]

        self.assertEqual(actual, expected)

    def test_get_markers(self):
        # Create marker
        factory = APIClient()
        request_body = {'latitude': 123.45678, 'longitude': -901.23456, 'altitude': 789.01234}

        factory.post('/markers/', request_body, format='json')

        # Get markers
        actual = factory.get('/markers/', format='json').data
        expected = [{'id': 1, 'latitude': Decimal('123.45678'), 'longitude': Decimal('-901.23456'), 'altitude': Decimal('789.01234')}]

        self.assertEqual(actual, expected)

    def test_delete_marker(self):
        # Create marker
        factory = APIClient()
        request_body = {'latitude': 123.45678, 'longitude': -901.23456, 'altitude': 789.01234}

        factory.post('/markers/', request_body, format='json')

        # Delete marker
        actual = factory.delete('/markers/1', format='json').data
        expected = []

        self.assertEqual(actual, expected)

    def test_clear_markers(self):
        # Create marker
        factory = APIClient()
        request_body = {'latitude': 123.45678, 'longitude': -901.23456, 'altitude': 789.01234}

        factory.post('/markers/', request_body, format='json')

        # Clear markers
        actual = factory.delete('/markers/', format='json').data
        expected = []

        self.assertEqual(actual, expected)