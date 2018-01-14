# -*- coding: utf-8 -*-
from django.forms import ModelForm
from PWJS_DjangoProject.szkola.models import Uczen

class StudentForm(ModelForm):

    class Meta:
        model = Uczen
        fields = '__all__'

        def clean(self):
            super().clean()