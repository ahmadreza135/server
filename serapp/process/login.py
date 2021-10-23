from django.views.decorators.csrf import csrf_protect ,csrf_exempt
from django.contrib.auth.models import User
from django.http import JsonResponse
from json.encoder import JSONEncoder
from django.contrib.auth import authenticate, login, logout

import django

@csrf_exempt
def login_user(request):
    Email = request.POST.get('email')
    Password = request.POST.get('password')
    Username = request.POST.get("username")
    print(Password)
    data = {}
    try:
        # user = User.objects.get(username=Username,password=Password)
        user = authenticate(username=Username, password=Password)
        if user is not None:
            if user.last_name == "true":
                data = {"loggedin" : "true"}
                user.last_name = "false"
                user.save()
            else:
                user.last_name = "true"
                user.save()
                data = {"login_user":"true"}
        else:
            # data = {"isnone":"yes"}  
            data = {"uis":User.objects.get(username=Email).password}     
    except django.contrib.auth.models.User.DoesNotExist: 
        data = {"user_exists": "false"}
    return JsonResponse(data,encoder=JSONEncoder)    
