import io
import csv
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import AddressBookList

class ContactList(LoginRequiredMixin, ListView):
    model = AddressBookList

    def get_queryset(self):
    	if self.request.user.is_authenticated:
    		return AddressBookList.objects.filter(author=self.request.user)
    	else:
    		return None

class ContactCreate(CreateView):
	
    def form_valid(self, form):
    	form.instance.author = self.request.user
    	return super(ContactCreate, self).form_valid(form)

    model = AddressBookList
    fields = ['fname', 'lname', 'cnumber', 'address']
    success_url = reverse_lazy('addressbooklist_list')

class ContactUpdate(UpdateView):
    model = AddressBookList
    fields = ['fname', 'lname', 'cnumber', 'address']
    success_url = reverse_lazy('addressbooklist_list')

class ContactDelete(DeleteView):
    model = AddressBookList
    success_url = reverse_lazy('addressbooklist_list')

@login_required
def contact_upload(request):
    template = "addressbook/contact_upload.html"

    prompt = {
        'order': 'Order of the CSV should be FirstName, LastName, ContactNo, Address'
    }

    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        message.error(request, 'This is not a csv file', extra_tags='excel')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, quotechar="|"):
        _, created = AddressBookList.objects.update_or_create(
            fname=column[0],
            lname=column[1],
            cnumber=column[2],
            address=column[3]
        )

    context = {}
    return render(request, template, context)

@login_required
def contact_download(request):
    items = AddressBookList.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="contact.csv"'

    writer = csv.writer(response)
    writer.writerow(['FirstName', 'LastName', 'ContactNo', 'Address'])

    for obj in items:
        writer.writerow([obj.fname, obj.lname, obj.cnumber, obj.address])

    return response

