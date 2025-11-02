from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthenticationTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.test_user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.register_url = reverse('signup')
        self.login_url = reverse('login')
        self.verify_url = reverse('token_refresh')

    def test_user_registration_success(self):
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpass123'
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertIn('user', response.data)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_user_registration_invalid_data(self):
        data = {'username': 'incomplete'}
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def test_user_login_success(self):
        data = {
            'username': 'testuser',
            'password': 'testpass123'
        }
        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertIn('user', response.data)

    def test_user_login_invalid_credentials(self):
        data = {
            'username': 'testuser',
            'password': 'wrongpass'
        }
        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_verify_user_with_token(self):
        login_data = {'username': 'testuser', 'password': 'testpass123'}
        login_response = self.client.post(self.login_url, login_data, format='json')
        token = login_response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.get(self.verify_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('user', response.data)

    def tearDown(self):
        self.client.credentials()
