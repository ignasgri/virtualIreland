from django.conf.urls import url
from .views import all_about

from .views import *

from . import views

urlpatterns = [
    url(r'^$', all_about, name='about'),
    url(r'^(?P<id>\d+)/$', abou_detail),
    # url(r'index/about^(?P<id>\d+)/$', abou_detail),
]