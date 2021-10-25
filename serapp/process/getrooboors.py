from django.http import JsonResponse
from serapp.models import arz_roo_boors
from django.views.decorators.csrf import csrf_protect ,csrf_exempt

@csrf_exempt
def get(request):
    if request.method=='GET':
        g = arz_roo_boors.objects.all()
        f = g.name
        dat = {"name":"f"}
        return JsonResponse(dat)