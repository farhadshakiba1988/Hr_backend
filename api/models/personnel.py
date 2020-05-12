from django.db import models

from api.models import Proposal

STATUS = (
    ('Active', 'پذیرفته شده'),
    ('InActive', 'بررسی نشده'),
    ('Failed', 'رد شده'),
)


class Personnel(models.Model):
    name = models.CharField(max_length=120)
    proposal_id = models.ForeignKey(Proposal, on_delete=models.CASCADE)
    insurance_sts = models.CharField(max_length=120)
    insurance_no = models.CharField(max_length=120)
    bank_account = models.CharField(max_length=120)
    bank_card_number = models.CharField(max_length=120)
    intro_checklist = models.CharField(max_length=120)
    equip_checklist = models.CharField(max_length=120)
    sts = models.CharField(choices=STATUS, max_length=10)
