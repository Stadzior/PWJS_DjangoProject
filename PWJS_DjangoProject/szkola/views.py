# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from PWJS_DjangoProject.szkola.models import Przedmiot, Uczen

# Create your views here.
def lectures(request):
        przedmioty = Przedmiot.objects.all()
        return render_to_response('lecture_list.html', {'przedmioty': przedmioty})

def lecture(request, id):
    try:
        przedmiot = Przedmiot.objects.get(pk=id)
        uczniowie = Uczen.objects.filter(przedmioty__in=[id])
        return render_to_response('single_lecture.html', {'przedmiot': przedmiot, 'uczniowie': uczniowie})
    except Przedmiot.Entry:
        return render_to_response('single_lecture.html', {'error': True})