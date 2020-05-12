from django.contrib.auth.models import User
from django.db import models

from api.models import Proposal
from api.models import Personnel


class ProposalEducation(models.Model):
    proposal_id = models.ForeignKey(Proposal, on_delete=models.CASCADE)
    personnel_id = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    trend = models.CharField(max_length=120)
    university = models.CharField(max_length=120)
    start_at = models.CharField(max_length=120)
    end_at = models.CharField(max_length=120)
    file_id = models.CharField(max_length=120)
    note = models.CharField(max_length=120)
    level = models.CharField(max_length=120)