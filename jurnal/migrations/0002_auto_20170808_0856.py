# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-08 08:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jurnal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jurnal',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jurnals', to=settings.AUTH_USER_MODEL),
        ),
    ]