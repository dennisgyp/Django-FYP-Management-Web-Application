# Generated by Django 3.0.3 on 2020-02-29 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logbook', '0008_auto_20200228_2201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='docfile',
            new_name='submission_file',
        ),
    ]
