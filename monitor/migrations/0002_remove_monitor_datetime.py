# Generated by Django 3.2.10 on 2021-12-16 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monitor',
            name='datetime',
        ),
    ]