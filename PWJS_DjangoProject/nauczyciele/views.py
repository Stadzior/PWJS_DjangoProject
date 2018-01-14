# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response, redirect
from PWJS_DjangoProject.szkola.models import Nauczyciel, Przedmiot
from PWJS_DjangoProject.nauczyciele.forms import TeacherForm

import logging

def teachers(request):
    nauczyciele = Nauczyciel.objects.all()
    return render(request, 'teachers_list.html', {'nauczyciele': nauczyciele})

def teacher(request, id):
    #try:
        nauczyciel = Nauczyciel.objects.get(pk=id)
        
        if request.method == 'POST':
            f = TeacherForm(request.POST, instance=nauczyciel)
            f.save()
            
        przedmioty = Przedmiot.objects.filter(nauczyciel=nauczyciel)
        return render(request, 'single_teacher.html', {'nauczyciel': nauczyciel, 'przedmioty': przedmioty})
    #except Exception:
    #    return render_to_response('single_lecture.html', {'error': True})

def delete_teacher(request, id):
    Nauczyciel.objects.get(pk=id).delete()
    return redirect('/teachers')


def edit_teacher(request, id):
    uczen = Nauczyciel.objects.get(pk=id)

    if request.method == 'POST':
            form = TeacherForm(request.POST, instance=Nauczyciel.objects.get(pk=id))
            form.save()
            return redirect('/teachers')
    else:
        form = TeacherForm(instance=Nauczyciel.objects.get(pk=id))
        return render(request, 'edit_form.html', {'form': form})