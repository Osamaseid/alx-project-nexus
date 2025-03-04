from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class RoleBasedAccessTests(APITestCase):
    def setUp(self):
        self.admin = User.objects.create_user(username="admin", password="adminpass", role="admin")
        self.user = User.objects.create_user(username="user", password="userpass", role="user")

        self.admin_token = str(RefreshToken.for_user(self.admin).access_token)
        self.user_token = str(RefreshToken.for_user(self.user).access_token)

    def test_admin_access(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.admin_token}')
        response = self.client.get("/api/me/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "admin")

    def test_user_access(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.user_token}')
        response = self.client.get("/api/me/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "user")
