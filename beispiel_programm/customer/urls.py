from django.conf.urls import patterns, url
from customer import views

urlpatterns = patterns('',
                       url(r'new$', views.NewCustomer.as_view(), name='new_customer'),
                       url(r'edit/(?P<pk>[\w-]+)$', views.EditCustomer.as_view(), name='edit_customer'),
                       url(r'$', views.IndexCustomer.as_view(), name='list_customer'),
                       )
