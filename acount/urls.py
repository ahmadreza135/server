from django.urls import path
from .process import setting

from django.views.generic import TemplateView

urlpatterns = [
    path("setting/",TemplateView.as_view(template_name="setting.html"),name="setting-acount")
]
