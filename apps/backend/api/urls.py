"""
URL routes for the API app.
"""
from django.urls import path
from .views import AnalyzeView


urlpatterns = [
    
    path('analyze/', AnalyzeView.as_view(), name='analyze'),
    
    
]
