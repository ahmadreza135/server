from django.urls import path,include
from siteapp.process.homepage import page
from django.views.generic.base import TemplateView
# import process
from django.views.generic import TemplateView
from . import views
from django.http import HttpResponse
import re

def imageview(request):
    path = "siteapp/statics/images/favicon.ico"
    # path="siteapp/images/"+re.findall(r".+\/(.+)",url)[0]
    try:
        with open(path, "rb") as f:
            return HttpResponse(f.read(), content_type="image/png")
    except:
        response = HttpResponse()
        response.write("hey")
        return response

urlpatterns = [
    path("",page,name = "nemdanom"),
    path("robots.txt",TemplateView.as_view(template_name="./robots.txt", content_type="text/plain"),name = "robots"),
    path("acount/",include("acount.urls")),
    path("statics/",include("siteapp.staticrls")),
    path("information/aboutus/",TemplateView.as_view(template_name="bottom/Aboutus.html"),name="aboutus"),
    path("information/contactus/",TemplateView.as_view(template_name="bottom/Contactus.html"),name="contactus"),
    path("favicon.ico",imageview,name="favicon"),
    path("information/privacypolicy/",TemplateView.as_view(template_name="bottom/Privacypolicy.html"),name="contactus")
]