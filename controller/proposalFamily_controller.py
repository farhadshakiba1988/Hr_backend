import fake
from django.http import JsonResponse


class ProposalFamilyController:
    @staticmethod
    def index(request):
        return JsonResponse(fake.data())