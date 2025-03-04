from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from jobs.models import Job
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class JobTests(APITestCase):
    def setUp(self):
        self.admin = User.objects.create_user(username="admin", password="adminpass", role="admin")
        self.user = User.objects.create_user(username="user", password="userpass", role="user")

        self.admin_token = str(RefreshToken.for_user(self.admin).access_token)
        self.user_token = str(RefreshToken.for_user(self.user).access_token)

        self.job = Job.objects.create(
            title="Software Engineer",
            company="Tech Corp",
            location="New York",
            category="IT",
            description="Develop software solutions",
            salary=90000,
            posted_by=self.admin
        )

    def test_list_jobs(self):
        response = self.client.get("/api/jobs/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_admin_can_create_job(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.admin_token}')
        response = self.client.post("/api/jobs/", {
            "title": "Data Scientist",
            "company": "AI Ltd",
            "location": "San Francisco",
            "category": "AI",
            "description": "Analyze data",
            "salary": 120000,
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_cannot_create_job(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.user_token}')
        response = self.client.post("/api/jobs/", {
            "title": "Data Scientist",
            "company": "AI Ltd",
            "location": "San Francisco",
            "category": "AI",
            "description": "Analyze data",
            "salary": 120000,
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
