import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ("Umum", "Umum"),
        ("Special Edition", "Special Edition"),
    ]

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="Umum")
    is_available = models.BooleanField(default=True)  # ganti dari is_featured

    # atribut tambahan
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name