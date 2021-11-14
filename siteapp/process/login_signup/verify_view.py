from django.shortcuts import render


def view_first(request):
    return render(request,"../templates/verify_first_view.html",{})