"""virtualIreland URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from main.views import get_index
from location import urls as location_urls
from accounts import urls as accounts_urls
from blog import urls as blog_urls
from accounts import reset_urls as reset_urls
from .settings import MEDIA_ROOT
from django.views import static

from rest_framework import routers
from location import views as loc_det_views
from search import urls as search_urls
# from search.views import do_search

router = routers.DefaultRouter()
router.register(r'location', loc_det_views.Set_LocationViewSet)

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'accounts/', include(accounts_urls)),
    url(r'^location/', include(location_urls)),
    url(r'user/', include(reset_urls)),
    url(r'^blog/', include(blog_urls)),
    url(r'^$', get_index, name='index'),
    # url(r'^index/', get_index, name='index'),
    # url(r'^index/about/', include(about_urls)),
    url(r'^media/(?P<path>.*)$', static.serve,{'document_root': MEDIA_ROOT}),
    url(r'^search/', include(search_urls)),
    


]
