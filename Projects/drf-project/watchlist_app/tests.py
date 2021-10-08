from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from watchlist_app.api import serializers
from watchlist_app import models

class StreamPlatformTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="example", password="Password@123") 
        self.token = Token.objects.get(user__username='example')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream = models.StreamPlatform.objects.create(name='Netflix', about="1º Platorm", website="https://www.netflix.com")


    def test_streamplatform_post_forbidden(self):

        data = {
            "name": "Netflix",
            "about": "1º Streaming Platform",
            "website": "https://www.netflix.com"
        }

        response = self.client.post(reverse("streamplataform-list"), data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_streamplatform_list(self):
        response = self.client.get(reverse("streamplataform-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_streamplatform_retrive(self):
        response = self.client.get(reverse("streamplataform-detail", args=(self.stream.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    