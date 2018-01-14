# -*- coding: utf-8 -*-
from django.forms import ModelForm
from PWJS_DjangoProject.szkola.models import Przedmiot

class LectureForm(ModelForm):

    class Meta:
        model = Przedmiot
        fields = '__all__'

        def clean(self):
            super().clean()