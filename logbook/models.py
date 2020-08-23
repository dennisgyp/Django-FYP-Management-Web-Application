from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import datetime

class LogBook(models.Model):
    STATUS = (
			('End', 'End'),
			('Pending', 'Pending'),
			('Ongoing', 'Ongoing'),
			)
    title=models.CharField(max_length=100,default="")
    description=models.TextField(max_length=1000,default="")
    coordinator = models.ForeignKey(User, on_delete=models.CASCADE,related_name='admin')
    end_date = models.DateField(u'Deadline', help_text=u'Deadline', null=True)
    status = models.CharField(max_length = 50, null=True, choices=STATUS, default = 'Pending')
    created = models.DateTimeField(editable=False, null=True)
    updated = models.DateTimeField(editable=False, null=True)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d',blank=True,null=True)

    @property
    def is_over(self):
        return datetime.date.today() > self.end_date


    def is_ongoing(self):
        if datetime.date.today() < self.end_date:
             return True
        return False


    def __str__(self):
        return self.title

    def save(self):
        # pylint: disable=maybe-no-member
        if not self.id:
            self.created = datetime.date.today()
        self.updated = datetime.datetime.today()
        super(LogBook, self).save()



    def get_absolute_url(self):
        return reverse('log-detail',kwargs={'pk':self.pk})

class Log(models.Model):
    logbook=models.ForeignKey(LogBook,on_delete=models.CASCADE)
    body=models.TextField(max_length=1000,null=True,blank=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    submission_date = models.DateField()
    comments = models.TextField(u'Textual Notes', help_text=u'Textual Notes', blank=True, null=True)
    submission_file = models.FileField(upload_to='documents/%Y/%m/%d',null=True,blank=True)


    def save(self):
        self.submission_date = datetime.date.today()
        super(Log, self).save()



    def get_absolute_url(self):
        return reverse('log-submission',kwargs={'pk':self.pk})
