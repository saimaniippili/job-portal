# Generated by Django 3.2 on 2021-05-04 17:27

import datetime
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
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(default=None, max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=200)),
                ('location', models.CharField(choices=[('Mumbai', 'Mumbai'), ('Bangalore', 'Bangalore'), ('Pune', 'Pune'), ('Remote', 'Remote')], max_length=50)),
                ('description', models.TextField(blank=True)),
                ('about', models.TextField(blank=True)),
                ('job_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('contract', models.CharField(choices=[('Part Time', 'Part Time'), ('Full Time', 'Full Time'), ('Freelance', 'Freelancer')], max_length=150)),
                ('is_published', models.BooleanField(default=True)),
                ('vacancy', models.CharField(max_length=10, null=True)),
                ('experience', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
                ('deadline', models.DateTimeField()),
                ('main_image', models.ImageField(upload_to='photos/%Y/%m%d/')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
