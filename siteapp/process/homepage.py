from django.shortcuts import render
from serapp.models import public_arz
from django.views.decorators.csrf import csrf_protect
# @csrf_protect?
def page(request):
    template_name = "../templates/homepage.html"
    g = public_arz.objects.all()
    g = g[len(g)-1]
    print(request.META.get("csrf_token"))
    context = {"rooboors":g.name+str(g.price)+str(g.market_cap)}
    return render(request, template_name, context)