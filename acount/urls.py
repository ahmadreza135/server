from django.urls import path
from .process import setting,delet_acount
from .process.login.login import login_user
from .process.sign_up.sign_up import signUp
from .process.sign_up.verify import verify_email
from django.views.generic import TemplateView

urlpatterns = [
    path("setting/",setting.view,name="setting-acount"),
    path("changepass/",setting.changepass,name="dslfj"),
    path("delacount/",delet_acount.delacount,name="dslfj"),
    path("login/login/",login_user,name="login_user"),
    path("login/",TemplateView.as_view(template_name="login/login.html"),name="login_view"),
    path("send_code/",verify_email.first,name="firs_verify"),
    path("sign_up/",TemplateView.as_view(template_name="verify_first_view.html"),name="signup_view"),
    path("sign_up/verif_mail/",verify_email.second,name="second_verify"),
    path("sign_up/sign/",signUp,name="sign"),
    path("forgetpass/",verify_email.forget_password,name="forgetpass")
]
