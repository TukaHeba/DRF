from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookListCreateAPIView, BookViewSet

"""
This module defines the URL patterns for the library API.
It sets up routing for both ViewSet-based and APIView-based endpoints.
"""

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'', BookViewSet)  

urlpatterns = [
    # APIView URLs
    path('custom/', BookListCreateAPIView.as_view()), 
    
    # ModelViewSet URLs
    path('', include(router.urls)),  
]
