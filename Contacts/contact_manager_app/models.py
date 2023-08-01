from django.db import models
from django.utils import timezone

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    # Add the email field here with default as timezone.now
    email = models.EmailField(default=timezone.now)