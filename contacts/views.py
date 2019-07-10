from django.shortcuts import render, redirect
from .models import Contact


def contact(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = Contact(first_name=first_name, last_name=last_name, email=email, phone=phone, subject=subject, message=message)

        contact.save()

        return redirect('home')
    else:
        return render(request, 'contacts/contacts.html')