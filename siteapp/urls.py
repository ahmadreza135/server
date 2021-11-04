from django.urls import path
# import process

from . import views

urlpatterns = [
    path("",views.index,name = "nemdanom")
]