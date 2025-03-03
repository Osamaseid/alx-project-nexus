
from django.urls import path, include
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Job Board API",
        default_version='v1',
        description="API documentation for the Job Board platform",
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    path('api/', include('jobs.urls')),
    path('api/auth/', include('users.urls')),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
]
