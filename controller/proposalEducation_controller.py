import fake
from django.http import JsonResponse


class ProposalEducationController:
    @staticmethod
    def index(request):
        return JsonResponse(fake.data())