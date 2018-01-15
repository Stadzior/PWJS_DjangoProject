# -*- coding: utf-8 -*-
from django.forms import ModelForm
from PWJS_Django.models import Teacher, Lecture, Student
from django import forms


class TeacherForm(ModelForm):

    class Meta:
        model = Teacher
        fields = '__all__'

        def clean(self):
            super().clean()


class LectureForm(ModelForm):

    class Meta:
        model = Lecture
        fields = '__all__'

        def clean(self):
            super().clean()


class StudentForm(ModelForm):

    class Meta:
        model = Student
        fields = '__all__'

        def clean(self):
            super().clean()


class SignStudentForm(forms.Form):
    name = forms.CharField(max_length=40)
