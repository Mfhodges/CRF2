# Generated by Django 2.1.5 on 2019-07-16 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_auto_20190712_2016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='canvassite',
            name='subaccount',
        ),
        migrations.RemoveField(
            model_name='canvassite',
            name='term',
        ),
        migrations.RemoveField(
            model_name='course',
            name='requested',
        ),
    ]