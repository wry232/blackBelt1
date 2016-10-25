# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='confirm_password',
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]