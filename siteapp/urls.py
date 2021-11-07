from django.urls import path
from siteapp.process.homepage import page
# import process

from . import views

urlpatterns = [
    path("",page,name = "nemdanom")
]