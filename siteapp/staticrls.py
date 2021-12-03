from django.urls import path,include,re_path
from django.http import HttpResponse
import re
from PIL import Image

def imageview(request):
    url = request.get_full_path()
    path = "siteapp/statics/images/"+re.findall(r".+\/(.+)",url)[0]
    # path="siteapp/images/"+re.findall(r".+\/(.+)",url)[0]
    try:
        with open(path, "rb") as f:
            return HttpResponse(f.read(), content_type="image/png")
    except:
        response = HttpResponse()
        response.write("hey")
        return response
def jsview(request):
    url = request.get_full_path()
    path = "siteapp/statics/jss/"+re.findall(r".+\/(.+)",url)[0]
    try:
        with open(path, "rb") as f:
            return HttpResponse(f.read(), content_type="application/x-javascript")
    except:
        response = HttpResponse()
        response.write("hey")
        return response
def cssview(request):
    url = request.get_full_path()
    path = "siteapp/statics/csss/"+re.findall(r".+\/(.+)",url)[0]
    if "bootstrap" in url:
        path = "siteapp/statics/csss/bootstrap/"+re.findall(r".+\/(.+)",url)[0]
    try:
        with open(path, "rb") as f:
            return HttpResponse(f.read(), content_type="text/css")
    except:
        response = HttpResponse()
        response.write("hey")
        return response

urlpatterns = [
    re_path(r"images/.+\.png",imageview,name="image"),
    re_path(r"jss/.+\.js",jsview,name="image"),
    re_path(r"csss/.+\.css",cssview,name="image")
]