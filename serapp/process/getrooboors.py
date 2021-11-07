from django.http import JsonResponse
# from serapp.models import arz_roo_boors
from serapp.models import public_arz
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_protect ,csrf_exempt

@csrf_exempt
def get_last(request):
    if request.method=='POST':
        # g = arz_roo_boors.objects.all()
        username = request.POST['username']
        password = request.POST['password']
        u = authenticate(request, password=password, username=username)
        if u is not None and u.last_name=="true": 
            g = public_arz.objects.all()
            g = g[len(g)-1]
            dat = {"name":g.name,"marketcap":g.market_cap,"price":g.price,"timeopened":g.timeopened,"timeclosed":g.timeclosing}
        else:
            dat = {"user_exist": "false"}
    else:
        dat = {"bad_request": "true"}        
                
    return JsonResponse(dat)
    