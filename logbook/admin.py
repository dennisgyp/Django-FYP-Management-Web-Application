from django.contrib import admin

# Register your models here.
from .models import LogBook,Log

admin.site.register(LogBook)
admin.site.register(Log)
