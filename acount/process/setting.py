from django.contrib.auth import authenticate, logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from siteapp.models import dashboard
from django.contrib.auth import authenticate


from django.http import HttpResponse
from django.shortcuts import redirect


@csrf_protect
def view(request):
    try:
        post = request.session['_old_post']
        username = post["username"]
        password = post["password"]
        u = authenticate(request,username=username,password=password)
        if u is not None:
            try:
                sucse = request.session["sucse"]
                request.session.pop("sucse")
                return render(request,"setting.html",{"sucse":sucse})
            except KeyError:
                 return render(request,"setting.html",{})
        else:
            pass
    except KeyError:
        pass
@csrf_protect
def changepass(request):
    post = request.session['_old_post']
    email = post["username"]
    password = request.POST["newpass"]
    us = dashboard.objects.get(username=email)
    us.set_password(password)
    us.save()
    request.session["sucse"] = "true"
    return redirect("/acount/setting/")

def logout_user(request):
    request.session["_old_post"].pop("username")
    request.session["_old_post"].pop("password")
    logout(request)
    return redirect("/login/")