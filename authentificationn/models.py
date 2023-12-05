from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add any additional fields you need
    # Example:
    birth_date = models.DateField(null=True, blank=True)
