from django.shortcuts import render

# Create your views here.

def index(request):
    template_name = "../templates/login.html"
    context = {}
    return render(request, template_name, context)
