# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponse
from PWJS_DjangoProject.szkola.models import Przedmiot, Uczen, Nauczyciel
from PWJS_DjangoProject.przedmioty.sign_student import SignStudentForm
from PWJS_DjangoProject.przedmioty.forms import LectureForm
from django.core.exceptions import ObjectDoesNotExist
import logging

def lectures(request):
    przedmioty = Przedmiot.objects.all()
    return render(request, 'lecture_list.html', {'przedmioty': przedmioty})

def lecture(request, id):
    try:
        form = SignStudentForm()
        przedmiot = Przedmiot.objects.get(pk=id)
        uczniowie = Uczen.objects.filter(przedmioty__in=[id])
        nauczyciele = Nauczyciel.objects.filter(przedmioty__in=[id])
        return render(request, 'single_lecture.html', {'przedmiot': przedmiot, 'uczniowie': uczniowie, 'nauczyciele': nauczyciele, 'form': form})
    except Przedmiot.Entry:
        return render_to_response('single_lecture.html', {'error': True})

def delete_lecture(request, id):
    Przedmiot.objects.get(pk=id).delete()
    return redirect('/lectures')

def edit_lecture(request, id):
    if request.method == 'POST':
            form = LectureForm(request.POST, instance=Przedmiot.objects.get(pk=id))
            form.save()
            return redirect('/lectures')
    else:
        form = LectureForm(instance=Przedmiot.objects.get(pk=id))
        return render(request, 'edit_form.html', {'form': form})

def sign_student(request, id):
    try:
        uczen = Uczen.objects.get(imie=request.POST['student_name'])
        uczen.przedmioty.add(id)
        uczen.save()
    except:
        uczen = Uczen(imie=request.POST['student_name'])
        uczen.save()
        uczen.przedmioty = [id]
        uczen.save()

    return redirect('/lectures/lecture/' + id)
