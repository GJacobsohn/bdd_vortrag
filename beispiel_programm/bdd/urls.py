from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bdd.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('home.urls', namespace="staticpages")),
    url(r'^customer/', include('customer.urls', namespace='customer')),
    url(r'^admin/', include(admin.site.urls)),

)
