from django.views.decorators.csrf import csrf_protect ,csrf_exempt
from django.contrib.auth.models import User
from django.http import JsonResponse
from json.encoder import JSONEncoder
from django.contrib.auth import authenticate, login, logout
import django

@csrf_exempt
def login_user(request):
    Password = request.POST.get('password')
    Username = request.POST.get("username")
    # u = User.objects.get(username=Username)
    # u.set_password("iman")
    # u.save()
    # print(Password)
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
            # data = {"isnone":"yes"}  
            data = {"login_user":"false"}     
    except django.contrib.auth.models.User.DoesNotExist: 
        data = {"user_exists": "false"}
    print (data,request.POST)
    return JsonResponse(data,encoder=JSONEncoder)
    # return data["loggedin"]
