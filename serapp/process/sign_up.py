
import random
import smtplib
import ssl
import django
from django.contrib.auth import authenticate, logout
from django.db import models
from serapp.models import emailv
import serapp.process.verifmail as verifmail
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.models import User


@csrf_exempt
def signUp(request):
    data = {}
    print(request)
    req = request.POST
    # We Have Email, Password and UserName
    # TODO : Email verification
    if "first_req" in request.POST and "email" in request.POST:
        u = authenticate(email=request.POST["email"])
        if u is not None:
            data = {"user_exist": "true"}
        else:
            r = verifmail.verify_email.first(request)
            data = r

    elif "email" in request.POST and \
            "password" in request.POST and "username" in request.POST:

        try:
            Email = req.get('email')

            NewPassword = req.get('newpassword')

            try:
                u = User.objects.get(username=Email)
            except User.DoesNotExist:
                u = None
            if u is not None and u.has_usable_password() and "newpassword" in request.POST:
                NowPassword = req.get('password')
                u = authenticate(username=Email, password=NowPassword)
                u.set_password(NewPassword)
                u.save()
            elif u is None and "verification_code" in request.POST:
                r = verifmail.verify_email.second(request)
                data = r

            else:
                data = {"sign_uped": "false"}

        except KeyError:
            data = {"wrong_req": "true"}
        except User.DoesNotExist:
            data = {"email_verifyed": "false"}
    else:
        data = {"wrong_requ": "true"}

    return JsonResponse(data)
