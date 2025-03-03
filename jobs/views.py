from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Job, Application
from .serializers import JobSerializer, ApplicationSerializer
from .permissions import IsAdminUser, IsJobApplicant
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Job

class JobListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'location']
    search_fields = ['title', 'description']

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminUser()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)

class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [IsAdminUser()]
        return [permissions.AllowAny()]

class ApplicationCreateView(generics.CreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsJobApplicant]

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)

class ApplicationListView(generics.ListAPIView):
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        if self.request.user.role == 'admin':
            return Application.objects.all()
        return Application.objects.filter(applicant=self.request.user)


