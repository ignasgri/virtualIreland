from django.shortcuts import render, get_object_or_404
from .models import Abou
from rest_framework import viewsets
from .serializers import AbouSerializer
from django.template.context_processors import csrf


# Create your views here.
def all_about(request):
    about = Abou.objects.all()
    args = {}
    args.update(csrf(request))
    return render(request, "about.html", {"about": about}, args)

def abou_detail(request, id):
    abou = get_object_or_404(Abou, pk=id)
    abou.views += 1
    abou.save()
    return render(request, "aboutdetail.html", {'abou': abou})


class AbouViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Abou.objects.all()
    serializer_class = AbouSerializer
