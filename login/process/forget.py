from django.shortcuts import render


def view(request):
    template_name = "login_signup/forgetpass.html"
    return render(request, template_name, {})