from django.contrib.auth.models import User
from django.db import models


class Log(models.Model):
    title = models.CharField(max_length=120)
    data = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.CharField(max_length=120)