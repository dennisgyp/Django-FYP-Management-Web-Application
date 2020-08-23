from django.forms import ModelForm
from django.forms import forms
from .models import Appointment


class DateInput(forms.DateInput):
    input_type = 'date'


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['date','start_time','end_time','location','supervisor','notes','status']
        widgets = {'date': DateInput(),
        }
