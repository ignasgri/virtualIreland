from django.shortcuts import render, get_object_or_404
from about.models import Abou


# Create your views here.
# def do_search(request):
#     about = Abou.objects.filter(name__contains=request.GET['search'])
#     return render(request, 'results.html', {'about':about})



# Create your views here.

# def do_search(request):
#     about = Abou.objects.filter(name__icontains=request.GET['q'])
#     return render(request, 'results.html', {'about': about})

def do_search(request):
    about = Abou.objects.filter()

    if request.GET.get('abou'):
        about = about.filter(name__contains=request.GET['abou'])
        return render(request, 'results.html', {'about': about})