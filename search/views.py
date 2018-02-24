from django.shortcuts import render, get_object_or_404
from location.models import Set_Location


# Create your views here.
def do_search(request):
    location = Set_Location.objects.filter(content__contains=request.GET['search'])
    return render(request, 'results.html', {'location':location})


