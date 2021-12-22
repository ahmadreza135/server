from django.shortcuts import render
from serapp.models import public_arz
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import requires_csrf_token

@requires_csrf_token
@csrf_protect
def page(request):
    template_name = "../templates/homepage.html"
    g = public_arz.objects.all()
    g = g[len(g)-1]
    try:
        post = request.session["_old_post"]
    except KeyError:
        post = {}
    context = {"arz":g,"arz_name":g.name,"arz_price":str(g.price),
            "arz_cap":str(g.market_cap),
                            "arz_time_open":g.timeopened,
                            "arz_time_close":g.timeclosing}
    if 'username' in post and 'password' in post:
        context["anacount"] = "true"
    else:
        context["anacount"] = "false"    
    return render(request, template_name, context)