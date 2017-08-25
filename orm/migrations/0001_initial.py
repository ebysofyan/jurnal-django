# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-09 00:55
from __future__ import unicode_literals

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
            name='Jurnal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=30)),
                ('keterangan', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jurnals', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'jurnal',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=30)),
                ('alamat', models.TextField()),
                ('tanggal_lahir', models.DateField()),
                ('photo', models.ImageField(upload_to='profile/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'profile',
            },
        ),
        migrations.CreateModel(
            name='Transaksi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField()),
                ('uraian', models.TextField()),
                ('debt', models.FloatField(default=0)),
                ('kredit', models.FloatField(default=0)),
                ('jurnal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaksis', to='orm.Jurnal')),
            ],
            options={
                'db_table': 'transaksi',
            },
        ),
    ]
