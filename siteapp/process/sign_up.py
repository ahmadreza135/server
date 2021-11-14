from django.contrib.auth import authenticate, logout
from django.db import models
from serapp.models import emailv
import serapp.process.verifmail as verifmail
from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from siteapp.models import dashboard as User




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
        print(request.user.username)

        try:
            Email = req.get('email')
            Email.index("@")

            NewPassword = req.get('newpassword')

            try:
                u = User.objects.get(username=Email)
            except User.DoesNotExist:
                u = None
            if u is not None and u.has_usable_password() and "newpassword" in request.POST:
                NowPassword = req.get('password')
                u = authenticate(username=Email, password=NowPassword)
                if u is not None:
                    u.set_password(NewPassword)
                    u.save()
                    data = {"sign_uped": "true"}
                    return render(request,"../templates/",data)
            elif u is None and "verification_code" in request.POST:
                r = verifmail.verify_email.second(request)
                data = r

            else:
                data = {"sign_uped": "false"}

        except KeyError:
            data = {"wrong_req": "true"}
        except User.DoesNotExist:
            data = {"email_verifyed": "false"}
        except ValueError:
            data = {"wrong_req": "true"}    

    elif "forget_pass" in request.POST and "email" in request.POST:
        r = verifmail.verify_email.forget_password(request)
        data = r
    else:
        data = {"wrong_requ": "true"}

    print (data)
    return JsonResponse(data)