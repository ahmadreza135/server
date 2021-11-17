from django.shortcuts import render


def view_first(request):
    return render(request,"login_signup/verify_first_view.html",{})