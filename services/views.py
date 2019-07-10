from django.views.generic import ListView
from .models import Service

class ServicesListView(ListView):
    queryset = Service.objects.all()
    template_name = 'services/services.html'
