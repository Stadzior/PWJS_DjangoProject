
from django.shortcuts import render, render_to_response, redirect
from PWJS_Django.models import Student, Lecture, Teacher
from PWJS_DjangoProject.forms import StudentForm, LectureForm, SignStudentForm, TeacherForm

# Student #


def students(request):

        if request.method == 'POST':
            f = StudentForm(request.POST)
            f.save()

        form = StudentForm()
        s = Student.objects.all()
        return render(request, 'students_list.html', {'students': s, 'form': form})
    #else:
    #    return render_to_response('lecture_list.html', {'error': True})


def student(request, id):
    #try:
        s = Student.objects.get(pk=id)
        l = Lecture.objects.filter(uczen__in=[id])
        return render_to_response('single_student.html', {'lectures': l, 'student': s})
    #except Exception:
    #    return render_to_response('single_lecture.html', {'error': True})


def delete_student(request, id):
    Student.objects.get(pk=id).delete()
    return redirect('/students')


def edit_student(request, id):
    s = Student.objects.get(pk=id)

    if request.method == 'POST':
            form = StudentForm(request.POST, instance=Student.objects.get(pk=id))
            form.save()
            return redirect('/students')
    else:
        form = StudentForm(instance=Student.objects.get(pk=id))
        return render(request, 'students_list.html', {'form': form})


# Lecture #


def lectures(request):
    l = Lecture.objects.all()
    return render(request, 'lecture_list.html', {'lectures': l})


def lecture(request, id):
    try:
        form = SignStudentForm()
        l = Lecture.objects.get(pk=id)
        s = Student.objects.filter(przedmioty__in=[id])
        t = Teacher.objects.filter(przedmioty__in=[id])
        return render(request, 'single_lecture.html', {'lecture': l, 'students': s, 'teachers': t, 'form': form})
    except Lecture.Entry:
        return render_to_response('single_lecture.html', {'error': True})


def delete_lecture(request, id):
    Lecture.objects.get(pk=id).delete()
    return redirect('/lectures')


def edit_lecture(request, id):
    if request.method == 'POST':
            form = LectureForm(request.POST, instance=Lecture.objects.get(pk=id))
            form.save()
            return redirect('/lectures')
    else:
        form = LectureForm(instance=Lecture.objects.get(pk=id))
        return render(request, 'edit_form.html', {'form': form})

def sign_student(request, id):
    try:
        s = Student.objects.get(imie=request.POST['student_name'])
        s.lectures.add(id)
        s.save()
    except:
        s = Student(imie=request.POST['student_name'])
        s.save()
        s.lectures = [id]
        s.save()

    return redirect('/lecture/' + id)

# Teacher #


def teachers(request):
    t = Teacher.objects.all()
    return render(request, 'teachers_list.html', {'teachers': t})


def teacher(request, id):
    # try:
    t = Teacher.objects.get(pk=id)

    if request.method == 'POST':
        f = TeacherForm(request.POST, instance=t)
        f.save()

    l = Lecture.objects.filter(nauczyciel=t)
    return render(request, 'single_teacher.html', {'teacher': t, 'lectures': l})
    # except Exception:
    #    return render_to_response('single_lecture.html', {'error': True})


def delete_teacher(request, id):
    Teacher.objects.get(pk=id).delete()
    return redirect('/teachers')


def edit_teacher(request, id):
    s = Teacher.objects.get(pk=id)

    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=Teacher.objects.get(pk=id))
        form.save()
        return redirect('/teachers')
    else:
        form = TeacherForm(instance=Teacher.objects.get(pk=id))
        return render(request, 'edit_form.html', {'form': form})
