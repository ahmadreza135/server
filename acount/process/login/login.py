from django.views.decorators.csrf import csrf_protect ,csrf_exempt
# from siteapp.models import dashboard as User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user_in
from django.http import JsonResponse,HttpResponseRedirect
from json.encoder import JSONEncoder
from django.shortcuts import redirect
from django.shortcuts import render

import django


@csrf_protect
def login_user(request):
    Password = request.POST.get('password')
    Username = request.POST.get("username")
    data = {}
    user = authenticate(request,username=Username, password=Password)
    
    if user is not None:
        user.last_name = "true"
        user.save()
        data = {"login_user":"true"}
        # TODO : set context
        # print(request.user)
        login_user_in(request,user)
        # logout(request)
        # print(request.user.is_authenticated)
        request.session['_old_post'] = request.POST
        return redirect("/acount/dashboard/")
        # return render(request,"dashboard.html",data)

        
    else:
        return render(request,"login/login.html",context={"error":"username-or-password-is-wrong"})
    