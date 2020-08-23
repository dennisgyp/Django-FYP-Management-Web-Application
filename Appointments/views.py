from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User,Group
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Appointment


# Create your views here.


def appointmentlist(request):
    context = {
        # pylint: disable=maybe-no-member
        'appointments': Appointment.objects.all()
    }

    return render(request,'appointments/user_appointment.html',context)

class AppointmentListView(LoginRequiredMixin,ListView):
    model = Appointment
    template_name='appointments/user_appointment.html'  # <app/<model>_<viewtype>.html
    context_object_name = 'appointments'
    ordering = ['-date']
    paginate_by = 3
    
    def get_queryset(self):
        user=self.request.user
        if user.groups.filter(name='student'):
            user=self.request.user
            # pylint: disable=maybe-no-member
            return Appointment.objects.filter(user=user)
        
        else:
              if user.groups.filter(name='supervisor'):
                  # pylint: disable=maybe-no-member
                  user=self.request.user
                  return Appointment.objects.filter(supervisor=user)



class AppointmentDetailView(LoginRequiredMixin,DetailView):
    model = Appointment
    

class AppointmentCreateView(LoginRequiredMixin,CreateView):
    model = Appointment
    fields = ['date','start_time','end_time','location','supervisor','notes']

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AppointmentUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Appointment
    fields = ['status']

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        appointment = self.get_object()
        if self.request.user == appointment.supervisor:
            return True
        return False

class AppointmentDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Appointment
    success_url ='/appointment/'

    def test_func(self):
        appointment = self.get_object()
        if self.request.user == appointment.user:
            return True
        return False

