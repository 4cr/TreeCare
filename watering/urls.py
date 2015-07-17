from django.conf.urls import patterns, url

from watering import views


urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^addcomment/$', views.addcomment, name='addcomment'),
)