from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.youtube.models import YoutubeURL


class YoutubeURLTestCase(APITestCase):

    def setUp(self):
        self.url = reverse('index')
        YoutubeURL.objects.create(url="https://www.youtube.com/watch?v=nSKp2StlS6s")
        YoutubeURL.objects.create(url="https://www.youtube.com/watch?v=Mq1MD5qXI08")

    def test_get_200(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data), 2)

    def test_post_201(self):
        data = {'url': 'https://www.youtube.com/watch?v=0vPt7GI-2kc'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_401(self):
        data = {'url': 'https://www.123456789'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
