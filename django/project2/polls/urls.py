from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns=[
    url(r'^$',views.IndexView.as_view(), name='index'),
    url(r'^polls/(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^polls/(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name="results"),
    url(r'^polls/(?P<pk>\d+)/vote/$', views.vote, name="vote"),

]
