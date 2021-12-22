from django.shortcuts import render

# Create your views here.

def login_view(request):
    try:
        context = request.session
        context = context["error_data"]
        request.session.pop("error_data")
    except KeyError:
        context = {}
    return render(request,"login/login.html",context)
def sign_up_view(request):
    try:
        context = request.session
        context = context["error_data"]
        request.session.pop("error_data")
    except KeyError:
        context = {}
    return render(request,"sign_up/verify_first_view.html",context)