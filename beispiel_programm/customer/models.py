
""" Customer Models """
from django.db import models

# Create your models here.


class Customer(models.Model):
    """ a Customer is represented by this Model. """
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)

    @property
    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        app_label = 'customer'


class PhoneCall(models.Model):
    """ a Customer Phone Call is represented by this Model """
    NICENESS_CHOICE = [('L', 'lovely'),
                       ('N', 'normal'),
                       ('R', 'rude'),
                       ('A', 'Asshole')]
    niceness_level = models.CharField(max_length=1, choices=NICENESS_CHOICE)

    class Meta:
        app_label = 'customer'