from django.contrib import auth
from django.contrib.auth import authenticate, logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from siteapp.models import dashboard
from django.contrib.auth import authenticate


from django.http import HttpResponse
from django.shortcuts import redirect


@csrf_protect
def view(request):
    print(request.session["_old_post"])
    try:
        post = request.session['_old_post']
        username = post["username"]
        password = post["password"]
        u = authenticate(request,username=username,password=password)
        if u is not None:
            try:
                sucse = request.session["sucse"]
                # request.session.pop("sucse")
                return render(request,"setting.html",{"sucse":sucse})
            except KeyError:
                 return render(request,"setting.html",{})
        else:
            pass
    except KeyError:
        return redirect("/acount/login/")
@csrf_protect
def changepass(request):
    data = request.POST
    post = request.session['_old_post']
    email = post["username"]
    oldpass = data["oldpass"]
    newpass = data["newpass"]
    confirmpass = data["confirmpass"]
    u = authenticate(request,username=email,password=oldpass)
    if u is not None:
        if newpass == confirmpass:
            u.set_password(newpass)
            u.save()
            # request.session["sucse"] = "true"
            post["password"] = newpass
            # print(post)
            request.session["_old_post"].pop("password")
            request.session["_old_post"]["password"] = newpass
            print(request.session["_old_post"])
            return redirect("/acount/settings/")


def logout_user(request):
    request.session["_old_post"].pop("username")
    request.session["_old_post"].pop("password")
    logout(request)
    return redirect("/")