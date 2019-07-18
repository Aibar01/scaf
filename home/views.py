from django.shortcuts import render, redirect
from projects.models import Project
from services.models import Service
from .models import Engineer, Review, Certificate, Clients


def home(request):
    projects = Project.objects.all()[:2]
    services = Service.objects.all()[:4]
    engineers = Engineer.objects.all()[:2]
    reviews = Review.objects.all().order_by('-hire_date')
    context = {
        'reviews': reviews,
        'projects': projects,
        'services': services,
        'engineers': engineers
    }

    return render(request, 'home/home_page.html', context)


def about(request):
    certificates = Certificate.objects.all()
    reviews = Review.objects.all().order_by('-hire_date')
    engineers = Engineer.objects.all()
    clients = Clients.objects.all()
    context = {
        'engineers': engineers,
        'reviews': reviews,
        'certificates': certificates,
        'clients': clients,
    }

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        description = request.POST.get('description')

        Review.objects.create(full_name=full_name, description=description).save()

        return redirect('home')
    else:
        return render(request, 'home/about_page.html', context)



