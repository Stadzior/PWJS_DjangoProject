# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

# Create your models here.
@python_2_unicode_compatible
class Przedmiot(models.Model):
    nazwa = models.CharField(max_length=140)

    def __str__(self):
        return u'{f}'.format(f=self.nazwa) 

@python_2_unicode_compatible
class Nauczyciel(models.Model):
    imie = models.CharField(max_length=40)
    przedmioty = models.ManyToManyField(Przedmiot)

    def __str__(self):
        return u'{f}'.format(f=self.imie) 

@python_2_unicode_compatible
class Uczen(models.Model):
    imie = models.CharField(max_length=40)
    przedmioty = models.ManyToManyField(Przedmiot)

    def __str__(self):
        return u'{f}'.format(f=self.imie) 