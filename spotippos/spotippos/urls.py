
from django.conf.urls import url

from properties import views

urlpatterns = [
    url(r'^api/v1/properties$', views.PropertyList.as_view()),
    url(r'^api/v1/properties/cordinates/(?P<ax>[0-9]+)/(?P<ay>[0-9]+)/(?P<bx>[0-9]+)/(?P<by>[0-9]+)/$', views.get_cordinates),
    url(r'^api/v1/properties/(?P<pk>[0-9]+)/$', views.PropertyDetail.as_view()),
]
