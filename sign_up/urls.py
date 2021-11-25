from django.urls import path
from django.views.generic.base import TemplateView
from sign_up.process.sign_up import signUp
from sign_up.process.verify import verify_email

urlpatterns = [
    path("send_code/",verify_email.first,name="firs_verify"),
    path("",TemplateView.as_view(template_name="verify_first_view.html"),name="signup_view"),
    path("verif_mail/",verify_email.second,name="second_verify"),
    path("sign/",signUp,name="sign"),
    path("forgetpass/",verify_email.forget_password,name="forgetpass"),
    
]