"""
URL routes for the API app.
"""
from django.urls import path
from django.http import HttpResponse
from .views import AnalyzeView

def empty_favicon(request):
    return HttpResponse(status=204)  # No Content

urlpatterns = [
    path('analyze/', AnalyzeView.as_view(), name='analyze'),
    path('favicon.ico', empty_favicon),  # Handles favicon requests gracefully
]
