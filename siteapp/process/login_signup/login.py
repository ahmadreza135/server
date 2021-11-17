from django.views.decorators.csrf import csrf_protect ,csrf_exempt
# from siteapp.models import dashboard as User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user
from django.http import JsonResponse,HttpResponseRedirect
from json.encoder import JSONEncoder
from django.shortcuts import redirect
from django.shortcuts import render

import django
import json

# @csrf_exempt
@csrf_protect
def login_view(request):

    # return HttpResponseRedirect("/json/rooboors/get/"

    return render(request,"login_signup/login.html",{"top":"top"})
# @csrf_exempt
@csrf_protect
def login(request):
    Password = request.POST.get('password')
    Username = request.POST.get("username")
    data = {}
    try:
        # user = User.objects.get(username=Username,password=Password)
        user = authenticate(request,username=Username, password=Password)
        
        if user is not None:
            user.last_name = "true"
            user.save()
            data = {"login_user":"true"}
            # TODO : set context
            # print(request.user)
            login_user(request,user)
            # logout(request)
            # print(request.user.is_authenticated)
            return redirect("/dashboard?username=ahmadrezaqasemi1384@gmail.com&password=ahmad")
            # return render(request,"dashboard.html",data)
    
            
        else:
            data = {"login_user":"false"}
            return render(request,"login_signup/login_faild.html",{})
    except django.contrib.auth.models.User.DoesNotExist: 
        data = {"user_exists": "false"}
        return render(request,"login_signup/login_faild.html",{})
    