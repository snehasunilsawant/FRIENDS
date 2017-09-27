from django.conf.urls import url , include

from . import views

urlpatterns = [

    url(r'^$', views.index),
    url(r'^add/(?P<friendid>\d+)/$', views.add),
    url(r'^remove/(?P<friendid>\d+)/$', views.remove),
    url(r'^user/(?P<userid>\d+)/$', views.show),
           
]