import models
from django.views import generic
from django.core.urlresolvers import reverse_lazy

class IndexCustomer(generic.ListView):
    """ List the Customers """
    model = models.Customer
    context_object_name = 'all_customers'


class NewCustomer(generic.CreateView):
    """ View for creating a Customer """
    model = models.Customer
    success_url = reverse_lazy('customer:list_customer')
    fields = ['first_name', 'last_name']


class EditCustomer(generic.UpdateView):
    """ View for Updating a Customer """
    model = models.Customer
    success_url = reverse_lazy('customer:list_customer')
    fields = ['first_name', 'last_name']
