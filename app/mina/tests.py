from django.test import TestCase
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APITestCase

from member.models import User
from mina.models import MinaPost


class MinaPostAPITest(APITestCase):
    URL = "/api/mina/"

    def test_create(self):
        user = baker.make(User)
        self.client.force_authenticate(user)
        data = {
            "title": "SampleTitle",
            "content": "SampleContent",
            "description": "SampleDescription",
        }
        response = self.client.post(self.URL, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
