from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
# from siteapp.models import dashboard as dashdash
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import redirect

# post = request.GET
@csrf_protect
def dashboard(request):
    data = {}
    if request.method == "GET":
        try:  
        	post = request.session['_old_post']
        except KeyError:
             return redirect('/login/')
        
        if "username" in post and "password" in post:
            username = post["username"]
            password = post["password"]
            user = authenticate(request,username=username,password=password)
            if user is not None:
                data = {"user":user}
                return render(request,"dashboard.html",data)
            else:
                data = {"user_exist":"true"}
        elif "newpassword" in post and "email" in post:
            username = post["email"]
            password = post["newpassword"]
            user = authenticate(request,username=username,password=password)
            if user is not None:
                data = {"user":user}
                return render(request,"dashboard.html",data)
        else:
            data = {"wrong_req":"true"}          
    else:
        return redirect('/login/')
    return JsonResponse(data)