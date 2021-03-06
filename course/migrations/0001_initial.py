# Generated by Django 2.1.5 on 2019-08-09 02:09

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
            name='Activity',
            fields=[
                ('name', models.CharField(max_length=40)),
                ('abbr', models.CharField(max_length=3, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'verbose_name': 'Activity Type',
                'verbose_name_plural': 'Activity Types',
            },
        ),
        migrations.CreateModel(
            name='AdditionalEnrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('TA', 'TA'), ('INST', 'Instructor'), ('DES', 'Designer'), ('LIB', 'Librarian'), ('OBS', 'Observer')], default='TA', max_length=4)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AutoAdd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('ta', 'TA'), ('instructor', 'Instructor'), ('designer', 'Designer'), ('librarian', 'Librarian')], max_length=10)),
            ],
            options={
                'ordering': ('user__username',),
            },
        ),
        migrations.CreateModel(
            name='CanvasSite',
            fields=[
                ('canvas_id', models.CharField(default=None, max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(default=None, max_length=50)),
                ('sis_course_id', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('workflow_state', models.CharField(default=None, max_length=15)),
                ('added_permissions', models.ManyToManyField(blank=True, default=None, related_name='added_permissions', to=settings.AUTH_USER_MODEL)),
                ('owners', models.ManyToManyField(blank=True, related_name='canvas_sites', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Canvas Site',
                'verbose_name_plural': 'Canvas Sites',
                'ordering': ('canvas_id',),
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('course_term', models.CharField(choices=[('A', 'Spring'), ('B', 'Summer'), ('C', 'Fall')], max_length=1)),
                ('course_code', models.CharField(editable=False, max_length=150, primary_key=True, serialize=False, unique=True)),
                ('course_number', models.CharField(max_length=4)),
                ('course_section', models.CharField(max_length=4)),
                ('course_name', models.CharField(max_length=250)),
                ('year', models.CharField(max_length=4)),
                ('requested', models.BooleanField(default=False)),
                ('requested_override', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('course_code',),
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('notice_heading', models.CharField(max_length=100)),
                ('notice_text', models.TextField(max_length=1000)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notices', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'updated_date',
            },
        ),
        migrations.CreateModel(
            name='PageContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('markdown_text', models.TextField(max_length=4000)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('penn_id', models.CharField(max_length=10, unique=True)),
                ('canvas_id', models.CharField(max_length=10, null=True, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('name', models.CharField(max_length=50, unique=True)),
                ('abbreviation', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('visible', models.BooleanField(default=True)),
                ('opendata_abbr', models.CharField(max_length=2)),
                ('canvas_subaccount', models.IntegerField(null=True)),
            ],
            options={
                'verbose_name': 'School // Sub Account',
                'verbose_name_plural': 'Schools // Sub Accounts',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('name', models.CharField(max_length=50, unique=True)),
                ('abbreviation', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('visible', models.BooleanField(default=True)),
                ('schools', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='course.School')),
            ],
            options={
                'verbose_name': 'Subject // Deptartment ',
                'verbose_name_plural': 'Subjects // Departments',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Tools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('visibility', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='UpdateLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('finished', models.DateTimeField(blank=True, null=True)),
                ('process', models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('course_requested', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='course.Course')),
                ('copy_from_course', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('title_override', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('additional_instructions', models.TextField(blank=True, default=None, null=True)),
                ('reserves', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('COMPLETED', 'Completed'), ('IN_PROCESS', 'In Process'), ('CANCELED', 'Canceled'), ('APPROVED', 'Approved'), ('SUBMITTED', 'Submitted'), ('LOCKED', 'Locked')], default='SUBMITTED', max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('masquerade', models.CharField(max_length=20, null=True)),
                ('canvas_instance', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='canvas', to='course.CanvasSite')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.AddField(
            model_name='course',
            name='course_activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='course.Activity'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_primary_subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Subject'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_schools',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='course.School'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='course.Subject'),
        ),
        migrations.AddField(
            model_name='course',
            name='crosslisted',
            field=models.ManyToManyField(blank=True, default=None, related_name='_course_crosslisted_+', to='course.Course'),
        ),
        migrations.AddField(
            model_name='course',
            name='instructors',
            field=models.ManyToManyField(blank=True, related_name='courses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='sections',
            field=models.ManyToManyField(blank=True, default=None, related_name='_course_sections_+', to='course.Course'),
        ),
        migrations.AddField(
            model_name='autoadd',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.School'),
        ),
        migrations.AddField(
            model_name='autoadd',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Subject'),
        ),
        migrations.AddField(
            model_name='autoadd',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='multisection_request',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='additional_sections', to='course.Request'),
        ),
        migrations.AddField(
            model_name='canvassite',
            name='request_instance',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.Request'),
        ),
        migrations.AddField(
            model_name='additionalenrollment',
            name='course_request',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='additional_enrollments', to='course.Request'),
        ),
    ]
