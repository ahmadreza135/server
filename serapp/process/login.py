from django.views.decorators.csrf import csrf_protect ,csrf_exempt
from django.contrib.auth.models import User
from django.http import JsonResponse,HttpResponseRedirect
from json.encoder import JSONEncoder
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
import django
import json

@csrf_exempt
# @csrf_protect
def login_user(request):

    # return HttpResponseRedirect("/json/rooboors/get/")
    Password = request.POST.get('password')
    Username = request.POST.get("username")
    data = {}
    try:
        # user = User.objects.get(username=Username,password=Password)
        user = authenticate(request,username=Username, password=Password)
        # login(request,user)
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip)
        
        if user is not None:
            user.last_name = "true"
            user.save()
            data = {"login_user":"true"}
    
            
        else:
            data = {"login_user":"false"}     
    except django.contrib.auth.models.User.DoesNotExist: 
        data = {"user_exists": "false"}
 

    return JsonResponse(data)
