from django.contrib.messages.context_processors import messages
from django.shortcuts import render, redirect
from requests import request

from App.forms import ContactForm
from App.models import Contact


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def resume(request):
    return render(request, 'resume.html')

def projects(request):
    return render(request, 'portfolio.html')

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    context = {'form': form}
    return render(request, 'contact.html', context)

def contact_list_view(request):
    qs = Contact.objects.all()
    print(qs)
    context = {'query': qs}
    return render(request, 'contact_list_view.html', context)

def contact_detail_view(request, id):
    obj = Contact.objects.get(pk=id)
    print(obj)
    context = {'object': obj}
    return render(request, 'contact_detail_view.html', context)

