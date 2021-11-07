from django.shortcuts import render

def page(request):
    template_name = "../templates/homepage.html"
    context = {"rooboors":"hey"}
    return render(request, template_name, context)