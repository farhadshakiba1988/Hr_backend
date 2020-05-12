from django.contrib.auth.models import User
from django.db import models


STATUS = (
    ('Active', 'پذیرفته شده'),
    ('InActive', 'بررسی نشده'),
    ('Failed', 'رد شده'),
)


class Proposal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ncode = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    jobs = models.CharField(max_length=120)
    gender = models.CharField(max_length=120)
    is_global = models.BooleanField(default=False)
    for_cities = models.CharField(max_length=120)
    father_name = models.CharField(max_length=120)
    iden_id = models.CharField(max_length=120)
    iden_serial = models.CharField(max_length=120)
    iden_place = models.CharField(max_length=120)
    birth_place = models.CharField(max_length=120)
    birth_date = models.CharField(max_length=120)
    marriage_sts = models.CharField(max_length=120)
    house_sts = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    mobile = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    phone_emergency = models.CharField(max_length=120)
    sts = models.CharField(choices=STATUS, max_length=10)
    phone_emergency_name = models.CharField(max_length=120)
    phone_emergency_related = models.CharField(max_length=120)
    commitment_file_id = models.CharField(max_length=120)