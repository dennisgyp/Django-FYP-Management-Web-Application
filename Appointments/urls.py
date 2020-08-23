from django.urls import path
from .views import (
    AppointmentListView,
    AppointmentDetailView,
    AppointmentCreateView,
    AppointmentUpdateView,
    AppointmentDeleteView,
    
)
from . import views



urlpatterns = [
    path('', AppointmentListView.as_view(),name='appointment-view'),
    path('<int:pk>/', AppointmentDetailView.as_view(),name='appointment-detail'),
    path('new/', AppointmentCreateView.as_view(),name='appointment-create'),
    path('<int:pk>/update/', AppointmentUpdateView.as_view(),name='appointment-update'),
     path('<int:pk>/delete/', AppointmentDeleteView.as_view(),name='appointment-delete'),
     
    
]
