
import random
import smtplib
import ssl
import django
from django.contrib.auth import authenticate, logout
from django.db import models
from serapp.models import emailv
import serapp.process.verifmail as verifmail
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_protect ,csrf_exempt
from django.contrib.auth.models import User

@csrf_exempt
def signUp(request):
    data = {}
    print(request)
    req = request.POST
    # We Have Email, Password and UserName
    # TODO : Email verification
    # if "first_req" in request.POST and "email" in request.POST:
        # u = authenticate(email=request.POST["email"])
        # if u is not None:
        #     data = {"user_exist":"true"}
        # else:
        #     
        #     r = verifmail.verify_email.first(request)
        #     data = r

    if "verification_code" in request.POST and "email" in request.POST:
        r = verifmail.verify_email.second(request)
        data = r
    elif "email" in request.POST and\
    "password" in request.POST and "username" in request.POST:
        try:
            Email = req.get('email')
    
            
            NewPassword = req.get('newpassword')
            
            u = authenticate(username=Email)
            if u is not None and u.has_usable_password():
                NowPassword = req.get('password')
                u = authenticate(username=Email,password=NowPassword)
            elif u is None:
                em = emailv.objects.get(email=Email)
                if em is not None:
                    u = User.objects.create_user(username=Email)
                    u.set_password(NewPassword)
                    u.last_name = "false"
                    u.save()
                    data = {"sign_uped":"true"}


                else:
                    data = {"email_verifyed":"false"}    

               
            
            else:
                data = {"sign_uped":"false"}

        except KeyError:
            data = {"wrong_req":"true"}
        except User.DoesNotExist:
            data = {"email_verifyed":"false"}
    else:
        data = {"wrong_req":"true"}


    return JsonResponse(data)