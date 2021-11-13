from django.urls import path
from siteapp.process.homepage import page
from siteapp.process.login import login_view as login
from siteapp.process.login import login as login_user
# import process

from . import views

urlpatterns = [
    path("",page,name = "nemdanom"),
    path("login/",login,name = "nedmdanoxm"),
    path("login/login/",login_user,name = "nedmdanosxm")
]