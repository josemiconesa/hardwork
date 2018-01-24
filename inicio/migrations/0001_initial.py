# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-28 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('codigo_postal', models.IntegerField()),
                ('asunto', models.CharField(max_length=80)),
                ('mensaje', models.CharField(max_length=500)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]