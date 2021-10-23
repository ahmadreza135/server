from django.shortcuts import render
import django
import random
import smtplib, ssl
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_protect ,csrf_exempt
from django.contrib.auth.models import User
# >>> user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')


@csrf_exempt
def index(request):
    print(request.POST.get("foo1"))
    return JsonResponse({"message":"message"})










 