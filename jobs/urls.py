from django.urls import path
from .views import JobListCreateView, JobDetailView, ApplicationCreateView, ApplicationListView

urlpatterns = [
      
    path('jobs/', JobListCreateView.as_view(), name='job-list'),
    path('jobs/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path('applications/', ApplicationListView.as_view(), name='application-list'),
    path('jobs/<int:job_id>/apply/', ApplicationCreateView.as_view(), name='apply-job'),
]
