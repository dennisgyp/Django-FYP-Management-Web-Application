# Generated by Django 3.0.3 on 2020-02-27 12:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LogBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('description', models.TextField(default='', max_length=1000)),
                ('start_date', models.DateField(editable=False, help_text='Start Date', null=True, verbose_name='Start Date')),
                ('end_date', models.DateField(editable=False, help_text='Deadline', null=True, verbose_name='Deadline')),
                ('status', models.CharField(choices=[('Late', 'Late'), ('Submitted', 'Submmited'), ('Ongoing', 'Ongoing')], default='Pending', max_length=50, null=True)),
                ('update', models.DateTimeField(editable=False, null=True)),
                ('docfile', models.FileField(null=True, upload_to='documents/%Y/%m/%d')),
                ('coordinator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(default='', max_length=1000)),
                ('submission_date', models.DateField()),
                ('comments', models.TextField(blank=True, help_text='Textual Notes', null=True, verbose_name='Textual Notes')),
                ('docfile', models.FileField(null=True, upload_to='documents/%Y/%m/%d')),
                ('LogBook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logbook.LogBook')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
