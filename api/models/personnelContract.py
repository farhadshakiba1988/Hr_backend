from django.db import models

from api.models import Personnel


class PersonnelContract(models.Model):
    personnel_id = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    salary = models.SmallIntegerField()
    worker_coupon = models.CharField(max_length=120)
    housing_allowance = models.CharField(max_length=120)
    right_attraction = models.CharField(max_length=120)
    right_guardianship = models.CharField(max_length=120)
    reason_termination = models.CharField(max_length=120)
    contract_file_id = models.CharField(max_length=120)