__author__ = 'gabriel'

from home import views
from django.conf.urls import patterns, url


urlpatterns = patterns('',
                       url(r'$', views.Homepage.as_view(template_name="home.html"), name='homepage'),
                       )
