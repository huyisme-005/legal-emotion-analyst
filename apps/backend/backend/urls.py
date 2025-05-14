"""
URL configuration for backend project.
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def empty_favicon(request):
    return HttpResponse(status=204)  # No Content

urlpatterns = [
    path('favicon.ico', empty_favicon),  # Handles favicon requests gracefully
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),   # Include your app's URLs here
]

