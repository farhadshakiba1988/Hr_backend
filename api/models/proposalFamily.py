from django.db import models

from api.models import Proposal


class ProposalFamily(models.Model):
    proposal_id = models.ForeignKey(Proposal, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    relation = models.CharField(max_length=120)
    edu_level = models.CharField(max_length=120)
    edu_title = models.CharField(max_length=120)
    job = models.CharField(max_length=120)