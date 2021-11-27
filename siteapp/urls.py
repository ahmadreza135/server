from django.urls import path,include
from siteapp.process.homepage import page
from django.views.generic.base import TemplateView
from siteapp.process.dashboard import dashboard
# import process
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("login/",include("login.urls")),
    path("sign_up/",include("sign_up.urls")),
    path("",page,name = "nemdanom"),
    path("robots.txt",TemplateView.as_view(template_name="./robots.txt", content_type="text/plain"),name = "robots"),
    path("dashboard/",dashboard,name = "nedmdanoxm"),
    path("acount/",include("acount.urls")),
    path("statics/images/",include("siteapp.imageurls")),
    path("information/aboutus",TemplateView.as_view(template_name="bottom/Aboutus.html"),name="aboutus"),
    path("information/contactus",TemplateView.as_view(template_name="bottom/Contactus.html"),name="contactus"),
    path("information/privacypolicy",TemplateView.as_view(template_name="bottom/Privacypolicy.html"),name="contactus")
]