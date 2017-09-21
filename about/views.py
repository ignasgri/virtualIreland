from django.shortcuts import render
from .models import Abou
from rest_framework import viewsets
from .serializers import AbouSerializer
from django.template.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def all_about(request):
    about = Abou.objects.all()
    paginator = Paginator(about, 5)
    page = request.GET.get('page')
    try:
        about = paginator.page(page)
    except PageNotAnInteger:
        about = paginator.page(1)
    except EmptyPage:
        about = paginator.page(paginator.num_pages)
    args = {}
    args.update(csrf(request))
    return render(request, "about.html", {"about": about}, args)




class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Abou.objects.all()
    serializer_class = AbouSerializer

