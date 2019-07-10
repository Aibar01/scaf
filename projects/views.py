from django.shortcuts import render
from django.views.generic import ListView

from .models import Project


class ProjectListView(ListView):
    queryset = Project.objects.all()
    template_name = 'projects/projects.html'
