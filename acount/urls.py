from django.urls import path
from .process import setting,delet_acount
from .process.login.login import login_user
from .process.sign_up.sign_up import signUp
from .process.sign_up.verify import verify_email
from django.views.generic import TemplateView
from .process.dashboard import dashboard
from .views import login_view,sign_up_view
from .process.cypto import buy,sell


urlpatterns = [
    path("settings/",setting.view,name="setting-acount"),
    path("dashboard/",dashboard,name = "nedmdanoxm"),
    path("changepass/",setting.changepass,name="dslfj"),
    path("delacount/",delet_acount.delacount,name="dslfj"),
    path("login/login/",login_user,name="login_user"),
    path("login/",login_view,name="login_view"),
    path("send_code/",verify_email.first,name="firs_verify"),
    path("sign_up/",sign_up_view,name="signup_view"),
    path("sign_up/verif_mail/",verify_email.second,name="sign_up/second_verify"),
    path("sign_up/signup/",signUp,name="sign"),
    path("forgetpass/",verify_email.forget_password,name="forgetpass"),
    path("logout/",setting.logout_user,name="logout"),
    path("exchange/",setting.changeexchangesite,name="sdf"),
    path("buycypto/",buy,name="buycypto")
]
