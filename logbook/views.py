from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, CreateView,DetailView,UpdateView,DeleteView
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import LogBookForm
from .models import LogBook,Log
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
import datetime
from django.utils import timezone

# Create your views here.



def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name,uploaded_file)
        context['url'] = fs.url(name)
    return render(request,'logs/upload.html')


class LogBookListView(LoginRequiredMixin,ListView):
    model = LogBook
    template_name = 'logbook/logbook_list.html'
    context_object_name = 'logbooks'
    paginate_by = 3
    ordering = ['-created']



class LogBookDetailView(LoginRequiredMixin,DetailView):
    model = LogBook



class LogBookCreateView(LoginRequiredMixin,CreateView):
    model = LogBook
    fields = ['title','description','end_date','docfile','status']

    def form_valid(self,form):
        form.instance.coordinator = self.request.user
        return super().form_valid(form)


class LogBookUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = LogBook
    fields = ['title','description','end_date','docfile']

    def form_valid(self,form):
        form.instance.coordinator = self.request.user
        return super().form_valid(form)

    def test_func(self):
        logbook = self.get_object()
        if self.request.user == logbook.coordinator:
            return True
        return False

class LogBookDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = LogBook
    success_url ='/logbook/'

    def test_func(self):
        logbook = self.get_object()
        if self.request.user == logbook.coordinator:
            return True
        return False


class LogDetailView(DetailView):
    model = Log

class LogCreateView(LoginRequiredMixin,CreateView):
    model = Log
    fields = ['body','submission_file']

    def form_valid(self,form):
        form.instance.student = self.request.user
        # pylint: disable=maybe-no-member
        form.instance.logbook = LogBook.objects.get(id=self.kwargs.get('pk'))
        return super().form_valid(form)


class LogUpdateView(LoginRequiredMixin,UpdateView):
    model = Log
    fields = ['body','submission_file']



    def form_valid(self,form):
        form.instance.student = self.request.user
        # pylint: disable=maybe-no-member
        return super().form_valid(form)


    def test_func(self):
        log = self.get_object()
        if self.request.user == log.coordinator:
            return True
        return False


class LogDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Log
    success_url ='/logbook/'

    def test_func(self):
        log = self.get_object()
        if self.request.user == log.student:
            return True
        return False
