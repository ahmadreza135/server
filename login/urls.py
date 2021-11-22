from django.urls import path
from django.views.generic.base import TemplateView
from login.process.login import login as login_user

urlpatterns = [
    path("login/",login_user,name="login_user"),
    path("",TemplateView.as_view(template_name="login.html"),name="login_user"),
]
