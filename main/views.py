from django.shortcuts import render
from about.models import Abou

def get_index(request):
    return render(request, "index.html")

def get_index(request):
    About = Abou.objects.all()
    return render(request, "index.html", {"about": about})