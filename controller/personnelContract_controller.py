import fake
from django.http import JsonResponse


class PersonnelContractController:
    @staticmethod
    def index(request):
        return JsonResponse(fake.data())