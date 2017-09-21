from django.conf.urls import url
from .views import all_about

urlpatterns = [
    url(r'^$', all_about, name='about'),
]