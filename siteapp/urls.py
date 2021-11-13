from django.urls import path
from siteapp.process.homepage import page
from siteapp.process.login import login_view as login
from siteapp.process.login import login as login_user
from siteapp.process.sign_up import signUp
from siteapp.process.verify import verify_email
from siteapp.process.verify_view import view_first
# import process

from . import views

urlpatterns = [
    path("",page,name = "nemdanom"),
    path("login/",login,name = "nedmdanoxm"),
    path("login/login/",login_user,name = "nedmdanosxm"),
    path("sign_up/view/",view_first,name = "nedmdanosxm"),
    path("sign_up/send_code/",verify_email.first,name = "nedmdanosxm"),
    path("sign_up/verif_mail/",verify_email.second,name = "nedmdanosxm"),
    path("sign_up/sign/",signUp,name = "nedmdanosxm")
]