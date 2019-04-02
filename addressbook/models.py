from django.db import models
from django.conf import settings
from django.urls import reverse

class AddressBookList(models.Model):
    """docstring for AddressBookList."""
    fname = models.CharField("First Name", max_length=100)
    lname = models.CharField("Last Name", max_length=100)
    cnumber = models.CharField("Contact Number", max_length=12)
    address = models.CharField("Address", max_length=250)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        return f'{self.fname} {self.lname} {self.cnumber} {self.address}'

    def get_absolute_url(self):
        return reverse('addressbooklist_update', kwargs={'pk': self.pk})
