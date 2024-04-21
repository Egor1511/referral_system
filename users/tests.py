from rest_framework.test import APITestCase, URLPatternsTestCase
from django.urls import reverse, path, include
from rest_framework import status
from users.urls import router_v1, urlpatterns

class SendPhoneNumberTest(APITestCase, URLPatternsTestCase):

    urlpatterns += urlpatterns

    def test_send_phone_number(self):
        url = reverse('send_phone_number-list')

        data_valid = {
            'phone_number': '1234567890'
        }
        response_valid = self.client.post(url, data_valid, format='json')
        self.assertEqual(response_valid.status_code, status.HTTP_200_OK)
        self.assertEqual(response_valid.data['message'], 'Auth code sent')

    def test_send_auth_code(self):
        url = reverse('send_auth_code-list')

        phone_number = '1234567890'
        self.client.post(reverse('send_phone_number-list'), {'phone_number': phone_number}, format='json')
        data_valid = {
            'auth_code': '1234'
        }
        response_valid = self.client.post(url, data_valid, format='json')
        self.assertEqual(response_valid.status_code, status.HTTP_200_OK)
        self.assertEqual(response_valid.data['message'], 'Phone number verified')

        data_invalid = {
            'phone_number': 'invalid_number'
        }
        response_invalid = self.client.post(url, data_invalid, format='json')
        self.assertEqual(response_invalid.status_code, status.HTTP_400_BAD_REQUEST)
