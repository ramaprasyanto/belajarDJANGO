from django.conf.urls import url

from . import views

urlpatterns=[
  url(r'^resent/$', views.resent),
  url(r'^$', views.index)

]