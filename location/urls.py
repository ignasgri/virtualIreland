from django.conf.urls import url
from .views import location

from .views import *

from . import views

urlpatterns = [
    url(r'^$', location, name='location'),
    url(r'^(?P<id>\d+)/$', location_details, name='location_details'),
    # url(r'^(?P<id>\d+)/$', abou_detail),
    
]