"""
URL routes for the API app.
"""
from django.urls import path,include
from django.http import HttpResponse
from .views import AnalyzeView

def empty_favicon(request):
    return HttpResponse(status=204)  # No Content

urlpatterns = [
    path('favicon.ico', empty_favicon),  # Handles favicon requests gracefully, must be before
    #any catch-all patterns
    path('analyze/', AnalyzeView.as_view(), name='analyze'),
    path('api/', include('api.urls')),
    
]
