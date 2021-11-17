from django.shortcuts import render
from serapp.models import public_arz
from django.views.decorators.csrf import csrf_protect
# @csrf_protect?
def page(request):
    template_name = "../templates/homepage.html"
    g = public_arz.objects.all()
    g = g[len(g)-1]
    # print(request.META.get("csrf_token"))

    context = {"arz_name":g.name,"arz_price":str(g.price),
               "arz_cap":str(g.market_cap),
                             "arz_time_open":g.timeopened,
                             "arz_time_close":g.timeclosing}
    return render(request, template_name, context)