from django.shortcuts import render
from location.models import Set_Location

# def get_index(request):
#     return render(request, "index.html")

def get_index(request):
    location = Set_Location.objects.all()
    return render(request, "index.html", {"location": location})
