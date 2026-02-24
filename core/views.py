from django.shortcuts import render, redirect
from .models import SiteSettings, Service
from .forms import ContactForm

def home(request):
    settings = SiteSettings.objects.first()
    services = Service.objects.all()
    return render(request, 'home.html', {
        'settings': settings,
        'services': services
    })

def about(request):
    settings = SiteSettings.objects.first()
    return render(request, 'about.html', {'settings': settings})

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')

    return render(request, 'contact.html', {'form': form})