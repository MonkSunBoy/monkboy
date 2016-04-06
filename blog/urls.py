from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.index, name='index'),
    url(r'^examples/$', views.examples, name='examples'),
    url(r'^page/$', views.page, name='page'),
    url(r'^another_page/$', views.another_page, name='another_page'),
    url(r'^contact/$', views.contact, name='contact'),
]
