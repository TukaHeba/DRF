from django.db import models

"""
This module defines the data models for the library application.
The Book model represents a book in the library system with its essential attributes.
"""

# Book model representing a book in the library system
class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    in_stock = models.BooleanField(default=True)

    # Returns the string representation of the book
    def __str__(self):
        return self.title