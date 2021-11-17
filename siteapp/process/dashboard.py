from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
# from siteapp.models import dashboard as dashdash
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import redirect

@csrf_protect
def dashboard(request):
	if request.method == "GET":
		post = request.GET
		if "username" in post and "password" in post:
			username = post["username"]
			password = post["password"]
			user = authenticate(request,username=username,password=password)
			if user is not None:
				
				# print(te)
				data = {"username":user.username}
				return render(request,"dashboard.html",data)


	else:
		return redirect('/login/')