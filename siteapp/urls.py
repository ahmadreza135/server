from django.urls import path
from siteapp.process.homepage import page
from siteapp.process.login_signup.login import login_view as login
from siteapp.process.login_signup.login import login as login_user
from siteapp.process.login_signup.sign_up import signUp
from siteapp.process.login_signup.verify import verify_email
from siteapp.process.login_signup.verify_view import view_first
from django.views.generic.base import TemplateView
from siteapp.process.dashboard import dashboard
# import process
from . import views

urlpatterns = [
    path("",page,name = "nemdanom"),
    path("robots.txt",TemplateView.as_view(template_name="./robots.txt", content_type="text/plain"),name = "robots"),
    path("dashboard/",dashboard,name = "nedmdanoxm"),
    path("login/",login,name = "nedmdanoxm"),
    path("login/login/",login_user,name = "nedmdanosxm"),
    path("sign_up/",view_first,name = "nedmdanosxm"),
    path("sign_up/send_code/",verify_email.first,name = "nedmdanosxm"),
    path("sign_up/verif_mail/",verify_email.second,name = "nedmdanosxm"),
    path("sign_up/sign/",signUp,name = "nedmdanosxm")
]