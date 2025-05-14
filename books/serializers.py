from rest_framework import serializers
from .models import Book

"""
This module contains the serializers for the library API.
Serializers convert complex data types (like Django models) to Python data types
that can be easily rendered into JSON, XML, or other content types.
"""

# Serializer for the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'