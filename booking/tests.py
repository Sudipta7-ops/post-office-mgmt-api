from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from accounts.models import User
from .models import SpeedPostBooking

class BookingAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            employee_id='EMP001',
            username='testuser',
            password='testpass123',
            role='admin'
        )
        self.client.force_authenticate(user=self.user)

    def test_create_booking_valid(self):
        data = {
            'article_number': 'EE123456789IN',
            'weight_grams': 500
        }
        response = self.client.post('/api/v1/bookings/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_booking_invalid_article_number(self):
        data = {
            'article_number': 'INVALID123',
            'weight_grams': 500
        }
        response = self.client.post('/api/v1/bookings/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_booking_invalid_weight(self):
        data = {
            'article_number': 'EE123456789IN',
            'weight_grams': 0
        }
        response = self.client.post('/api/v1/bookings/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_bookings(self):
        response = self.client.get('/api/v1/bookings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_access(self):
        self.client.force_authenticate(user=None)
        response = self.client.get('/api/v1/bookings/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)