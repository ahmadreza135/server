from django.http import JsonResponse
from serapp.models import arz_roo_boors
from django.views.decorators.csrf import csrf_protect ,csrf_exempt

@csrf_exempt
def get_last(request):
    if request.method=='GET':
        g = arz_roo_boors.objects.all()
        g = g[len(g)-1]
        dat = {"name":g.name,"marketcap":g.market_cap,"price":g.price,"time":g.timeclosed}
        return JsonResponse(dat)

    