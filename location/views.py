from django.shortcuts import render, get_object_or_404
from .models import Set_Location
from rest_framework import viewsets
from .serializers import Set_LocationSerializer
from django.template.context_processors import csrf


# Create your views here.
def location(request):
    location = Set_Location.objects.all()
    args = {}
    args.update(csrf(request))
    return render(request, "location.html", {"location": location}, args)

def location_details(request, id):
    set_loc = get_object_or_404(Set_Location, pk=id)
    set_loc.views += 1
    set_loc.save()
    return render(request, "location_details.html", {'set_loc': set_loc})


class Set_LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Set_Location.objects.all()
    serializer_class = Set_LocationSerializer
