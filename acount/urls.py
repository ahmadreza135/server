from django.urls import path
from .process import setting,delet_acount
from .process.login.login import login_user
from .process.sign_up.sign_up import signUp
from .process.sign_up.verify import verify_email
from django.views.generic import TemplateView
from .process.dashboard import dashboard

urlpatterns = [
    path("settings/",setting.view,name="setting-acount"),
    path("dashboard/",dashboard,name = "nedmdanoxm"),
    path("changepass/",setting.changepass,name="dslfj"),
    path("delacount/",delet_acount.delacount,name="dslfj"),
    path("login/login/",login_user,name="login_user"),
    path("login/",TemplateView.as_view(template_name="login/login.html"),name="login_view"),
    path("send_code/",verify_email.first,name="firs_verify"),
    path("sign_up/",TemplateView.as_view(template_name="sign_up/verify_first_view.html"),name="signup_view"),
    path("sign_up/verif_mail/",verify_email.second,name="sign_up/second_verify"),
    path("sign_up/sign/",signUp,name="sign"),
    path("forgetpass/",verify_email.forget_password,name="forgetpass")
]
