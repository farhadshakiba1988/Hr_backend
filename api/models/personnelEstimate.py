from django.contrib.auth.models import User
from django.db import models

from api.models import Personnel


class PersonnelEstimate(models.Model):
    personnel_id = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.CharField(max_length=120)
    score_var = models.CharField(max_length=120)
    note = models.CharField(max_length=120)
