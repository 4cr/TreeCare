from django.conf.urls import patterns, include, url
from django.contrib import admin
from watering import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'treecare.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('watering.urls', namespace='watering')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^accounts/logout/$', views.LogoutView.as_view(), name='logout'),
)
