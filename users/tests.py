from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase

from users.models import UserProfile
from users.urls import urlpatterns


class Tests(APITestCase, URLPatternsTestCase):
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
        self.client.post(reverse('send_phone_number-list'),
                         {'phone_number': phone_number}, format='json')
        data_valid = {
            'auth_code': '1234'
        }
        response_valid = self.client.post(url, data_valid, format='json')
        self.assertEqual(response_valid.status_code, status.HTTP_200_OK)
        self.assertEqual(response_valid.data['message'],
                         'Phone number verified')

    def test_send_invalid_auth_code(self):
        url = reverse('send_auth_code-list')

        phone_number = '1234567890'
        self.client.post(reverse('send_phone_number-list'),
                         {'phone_number': phone_number}, format='json')
        data_invalid = {
            'phone_number': 'invalid_number'
        }
        response_invalid = self.client.post(url, data_invalid, format='json')
        self.assertEqual(response_invalid.status_code,
                         status.HTTP_400_BAD_REQUEST)

    def test_get_profile(self):
        self.profile = UserProfile.objects.create(
            phone_number='1234567890',
            invite_code='ABCDE1'
        )
        self.url = reverse('profile-detail', kwargs={'pk': self.profile.pk})
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['phone_number'], '1234567890')

    def test_update_profile_used_invite_code(self):
        self.profile = UserProfile.objects.create(
            phone_number='1234567890',
            invite_code='ABCDE1'
        )
        self.second_profile = UserProfile.objects.create(
            phone_number='1234567891',
            invite_code='DSFDS1'
        )
        data = {
            'used_invite_code': 'DSFDS1'
        }
        self.url = reverse('profile-detail', kwargs={'pk': self.profile.pk})
        response = self.client.patch(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_profile = UserProfile.objects.get(pk=self.profile.pk)
        self.assertEqual(updated_profile.used_invite_code, 'DSFDS1')

    def test_equal_update_profile_used_invite_code(self):
        self.profile = UserProfile.objects.create(
            phone_number='1234567890',
            invite_code='ABCDE1'
        )
        data = {
            'used_invite_code': 'ABCDE1'
        }
        self.url = reverse('profile-detail', kwargs={'pk': self.profile.pk})
        response = self.client.patch(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
