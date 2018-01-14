from django.contrib import admin
from PWJS_Django.models import Student, Lecture, Teacher

admin.site.register(Teacher)
admin.site.register(Lecture)
admin.site.register(Student)