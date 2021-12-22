from django.http import HttpResponse,JsonResponse
from django.shortcuts import render


def handler_404(request,exception):
    template_name = "page_404.html"
    r = render(request,template_name)
    r.status_code = 404
    return r