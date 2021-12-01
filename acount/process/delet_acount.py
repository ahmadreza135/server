from siteapp.models import dashboard
from django.shortcuts import redirect


def delacount(request):
    u = dashboard.objects.get(username=request.user,password=request.POST["password"])
    u.delete()
    return redirect("/login/")
    