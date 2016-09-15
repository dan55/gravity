# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-15 01:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gravapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_character', to='gravapp.Character')),
                ('character_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_character', to='gravapp.Character')),
            ],
        ),
    ]
