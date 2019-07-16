from django.views.generic import ListView, DetailView
from .models import Service


class ServicesListView(ListView):
    queryset = Service.objects.all()
    template_name = 'services/services.html'


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services/service_detail.html'
