from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField()
    name = models.CharField(max_length=50)
    bio = models.TextField(min_length=255)