import fake
from django.http import JsonResponse


class PersonnelEstimateController:
    @staticmethod
    def index(request):
        return JsonResponse(fake.data())
