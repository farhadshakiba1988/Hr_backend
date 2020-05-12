from django.forms.models import model_to_dict
from django.http import JsonResponse

from api.models import Proposal


class RegisterController:
    @staticmethod
    def index(request):
        return JsonResponse(True)

    @staticmethod
    def jobs(request):
        return JsonResponse(True)

    @staticmethod
    def ncode(request):
        model = Proposal.objects.filter(ncode__icontains=request.POST['ncode'])[0]
        if not model:
            return JsonResponse({'has': False}, safe=False)
        return JsonResponse({'has': True, 'record': model_to_dict(model)}, safe=False)

    @staticmethod
    def upload(request):
        return JsonResponse(True)

    @staticmethod
    def save(request):
        return JsonResponse(True)
