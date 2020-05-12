from django.db import models
from api.models import Proposal
from api.models import Personnel

STATUS = (
    ('Active', 'پذیرفته شده'),
    ('InActive', 'بررسی نشده'),
    ('Failed', 'رد شده'),
)


class ProposalInterview(models.Model):
    proposal_id = models.ForeignKey(Proposal, on_delete=models.CASCADE)
    personnel_id = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=120)
    interviewer = models.CharField(max_length=120)
    type = models.CharField(max_length=120)
    score = models.CharField(max_length=120)
    result = models.CharField(max_length=120)
    note = models.CharField(max_length=120)
    sts = models.CharField(choices=STATUS, max_length=10)
    interview_at = models.CharField(max_length=120)
