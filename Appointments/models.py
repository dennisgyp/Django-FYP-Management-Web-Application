from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Appointment(models.Model):
    STATUS = (
			('Pending', 'Pending'),
			('Approved', 'Approved'),
			('Rejected', 'Rejected'),
			)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='student')
    date = models.DateField(u'Date', help_text=u'yyyy/mm/dd')
    start_time = models.TimeField(u'Starting time', help_text=u'24hr format')
    end_time = models.TimeField(u'Final time', help_text=u'24hr format')
    location=models.CharField(max_length=50,null=True)
    supervisor=models.ForeignKey(User,related_name='supervisor', on_delete=models.CASCADE,null=True)
    notes = models.TextField(u'Textual Notes', help_text=u'Textual Notes', blank=True, null=True)
    status = models.CharField(max_length = 50, null=True, choices=STATUS, default = 'Pending')


    def get_absolute_url(self):
        return reverse('appointment-detail',kwargs={'pk':self.pk})
