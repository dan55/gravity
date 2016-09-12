from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Character(models.Model):
    first_name = models.CharField(max_length=48)
    last_name = models.CharField(max_length=48)

class Relationship(models.Model):
    character_1 = models.ForeignKey('Character', related_name='first_character')
    character_2 = models.ForeignKey('Character', related_name='second_character')