from django.shortcuts import redirect
from django.contrib.auth import authenticate

def buy(request):
    try:
        sessions = request.session["_old_post"]
        username = sessions["username"]
        password = sessions["password"]
    except KeyError:
        return redirect("/acount/login?return=/acount/buy/")
    user = authenticate(request,username = username,password = password)
    if user is not None:
        sarafi = user.sarafi
    else:
        return redirect("/acount/login/")

    return redirect(sarafi)    

def sell(request):
    pass