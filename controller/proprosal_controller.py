import fake as fake
from django.http import JsonResponse


class ProposalController:
    @staticmethod
    def index(request):
        return JsonResponse(fake.data())