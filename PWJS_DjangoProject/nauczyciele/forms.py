# -*- coding: utf-8 -*-
from django.forms import ModelForm
from PWJS_DjangoProject.szkola.models import Nauczyciel

class TeacherForm(ModelForm):

    class Meta:
        model = Nauczyciel
        fields = '__all__'

        def clean(self):
            super().clean()