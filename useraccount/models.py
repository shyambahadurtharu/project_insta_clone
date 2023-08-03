from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    contact = models.CharField(max_length=255, blank=True, default="")
    address = models.CharField(max_length=255, blank=True, default="")
    profile_picture = models.ImageField(
        upload_to="profile_pictures/",
        blank=True,
        null=True,
    )