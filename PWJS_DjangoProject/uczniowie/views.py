# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response, redirect
from PWJS_DjangoProject.szkola.models import Uczen,Przedmiot
from PWJS_DjangoProject.uczniowie.forms import StudentForm

# Create your views here.
def students(request):

        if request.method == 'POST':
            f = StudentForm(request.POST)
            f.save()

        form = StudentForm()
        uczniowie = Uczen.objects.all()
        return render(request, 'students_list.html', {'uczniowie': uczniowie, 'form': form})
    #else:
    #    return render_to_response('lecture_list.html', {'error': True})

def student(request, id):
    #try:
        uczen = Uczen.objects.get(pk=id)
        przedmioty = Przedmiot.objects.filter(uczen__in=[id])
        return render_to_response('single_student.html', {'przedmioty': przedmioty, 'uczen': uczen})
    #except Exception:
    #    return render_to_response('single_lecture.html', {'error': True})

def delete_student(request, id):
    Uczen.objects.get(pk=id).delete()
    return redirect('/students')

def edit_student(request, id):
    uczen = Uczen.objects.get(pk=id)

    if request.method == 'POST':
            form = StudentForm(request.POST, instance=Uczen.objects.get(pk=id))
            form.save()
            return redirect('/students')
    else:
        form = StudentForm(instance=Uczen.objects.get(pk=id))
        return render(request, 'students_list.html', {'form': form})
    