from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class AuthTests(APITestCase):
    def setUp(self):
        self.register_url = "/api/auth/register/"
        self.login_url = "/api/auth/login/"
        self.user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpassword",
            "role": "user",
        }
        self.admin_data = {
            "username": "adminuser",
            "email": "admin@example.com",
            "password": "adminpassword",
            "role": "admin",
        }
        self.user = User.objects.create_user(**self.user_data)
        self.admin = User.objects.create_user(**self.admin_data)

    def test_user_registration(self):
        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["username"], self.user_data["username"])

    def test_user_login(self):
        response = self.client.post(self.login_url, {
            "username": self.user_data["username"],
            "password": self.user_data["password"],
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class AuthTests(APITestCase):
    def setUp(self):
        self.register_url = "/api/auth/register/"
        self.login_url = "/api/auth/login/"
        self.user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpassword",
            "role": "user",
        }
        self.admin_data = {
            "username": "adminuser",
            "email": "admin@example.com",
            "password": "adminpassword",
            "role": "admin",
        }
        self.user = User.objects.create_user(**self.user_data)
        self.admin = User.objects.create_user(**self.admin_data)

    def test_user_registration(self):
        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["username"], self.user_data["username"])

    def test_user_login(self):
        response = self.client.post(self.login_url, {
            "username": self.user_data["username"],
            "password": self.user_data["password"],
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

