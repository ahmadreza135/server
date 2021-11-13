from django.views.decorators.csrf import csrf_protect ,csrf_exempt
from django.contrib.auth.models import User
from django.http import JsonResponse,HttpResponseRedirect
from json.encoder import JSONEncoder
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
import django
import json

# @csrf_exempt
@csrf_protect
def login_view(request):

    # return HttpResponseRedirect("/json/rooboors/get/"

    return render(request,"../templates/login.html",{"top":"top"})
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
            return render(request,"../templates/dashboard.html",data)
    
            
        else:
            data = {"login_user":"false"}
            return render(request,"../templates/login_faild.html",{})
    except django.contrib.auth.models.User.DoesNotExist: 
        data = {"user_exists": "false"}
        return render(request,"../templates/login_faild.html",{})
    