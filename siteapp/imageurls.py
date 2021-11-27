from django.urls import path,include,re_path
from django.http import HttpResponse
import re
from PIL import Image

def imageview(request):
    url = request.get_full_path()
    path = "siteapp/images/"+re.findall(r".+\/(.+)",url)[0]
    # path="siteapp/images/"+re.findall(r".+\/(.+)",url)[0]
    try:
        with open(path, "rb") as f:
            return HttpResponse(f.read(), content_type="image/png")
    except:
        response = HttpResponse()
        response.write("hey")
        return response

urlpatterns = [
    re_path(r".+\.png",imageview,name="image")
]