# yourproject/urls.py

from django.contrib import admin
from django.urls import path, include

from myapp.views import StudentViewSet  # Import your app's viewset

# Assuming you're using DefaultRouter from DRF
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
