from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Lecture(models.Model):
    name = models.CharField(max_length=140)

    def __str__(self):
        return u'{f}'.format(f=self.nazwa)

@python_2_unicode_compatible
class Teacher(models.Model):
    name = models.CharField(max_length=40)
    lectures = models.ManyToManyField(Lecture)

    def __str__(self):
        return u'{f}'.format(f=self.imie)

@python_2_unicode_compatible
class Student(models.Model):
    name = models.CharField(max_length=40)
    lectures = models.ManyToManyField(Lecture)

    def __str__(self):
        return u'{f}'.format(f=self.imie)