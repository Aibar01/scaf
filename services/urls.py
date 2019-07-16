from django.urls import path
from . import views


urlpatterns = [
    path('', views.ServicesListView.as_view(), name='services'),
    path('<int:pk>/', views.ServiceDetailView.as_view(), name='service_detail'),
]
