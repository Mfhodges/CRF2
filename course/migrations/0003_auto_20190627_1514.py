# Generated by Django 2.1.5 on 2019-06-27 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20190626_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='id',
        ),
        migrations.AlterField(
            model_name='activity',
            name='abbr',
            field=models.CharField(max_length=3, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='course.Activity'),
        ),
    ]