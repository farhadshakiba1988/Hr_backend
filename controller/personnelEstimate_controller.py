import fake
from django.http import JsonResponse


class PersonnelEstimateController:

    @staticmethod
    def list(request):
        return JsonResponse(fake.data())

    @staticmethod
    def delete(request):
        return JsonResponse(True)

    @staticmethod
    def update(request):
        return JsonResponse(True)

    @staticmethod
    def create(request):
        return JsonResponse(True)
