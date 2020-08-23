from .models import LogBook,Log
from django import forms
from django.forms import ModelForm

class DateInput(forms.DateInput):
    input_type = 'date'


class LogBookForm(ModelForm):
    class Meta:
        model = LogBook
        fields = ('title','description','end_date','docfile','status')
        widgets = {'end_date': DateInput(),
        }

class LogForm(ModelForm):
    class Meta:
        model = Log
        fields = ('body','submission_file')
