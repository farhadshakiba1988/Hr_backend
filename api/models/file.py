from django.contrib.auth.models import User
from django.db import models


class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    storage = models.CharField(max_length=120)
    filename = models.CharField(max_length=120)
    title = models.CharField(max_length=120)