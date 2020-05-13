import fake
from django.http import JsonResponse


class ProposalInterviewController:
    @staticmethod
    def index(request):
        return JsonResponse(fake.data())