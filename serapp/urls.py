from django.urls import path

import serapp.process.sign_up as sign_up
import serapp.process.verifmail as verifmail
import serapp.process.login as login
# import process

from . import views

urlpatterns = [
    path('login/login/',login.login_user, name='verify'),
    path('login/signup/',sign_up.signUp,name = "signup")
]