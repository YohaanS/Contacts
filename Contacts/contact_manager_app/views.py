# contact_manager_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm

def get_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_manager_app/contact_list.html', {'contacts': contacts})


def get_contact(request, pk):
    try:
        contact = Contact.objects.get(pk=pk)
        return render(request, 'contact_manager_app/contact_detail.html', {'contact': contact})
    except Contact.DoesNotExist:
        return render(request, 'contact_manager_app/contact_not_found.html')


def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts_list')  # Assuming you have a URL pattern named 'contacts_list'
    else:
        form = ContactForm()

    return render(request, 'contact_manager_app/add_contact.html', {'form': form})

def update_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('get_contact', pk=contact.pk)  # Use 'contact_detail' here
    else:
        form = ContactForm(instance=contact)

    return render(request, 'contact_manager_app/contact_update.html', {'form': form})
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)

    if request.method == 'POST':
        contact.delete()
        return redirect('contacts_list')  # Redirect to the contact list page after successful deletion

    return render(request, 'contact_manager_app/contact_confirm_delete.html', {'contact': contact})

def delete_all_contacts(request):
    if request.method == 'POST':
        Contact.objects.all().delete()
        return redirect('contacts_list')  # Redirect to the contact list page after successful deletion

    return render(request, 'contact_manager_app/delete_all_contacts.html')