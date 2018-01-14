import PWJS_DjangoProject.uczniowie.views
from django.conf.urls import url
urlpatterns = [
    url(r'^$', PWJS_DjangoProject.uczniowie.views.students),
    url(r'^student/(?P<id>[0-9]+)/', PWJS_DjangoProject.uczniowie.views.student),
    url(r'^student/delete/(?P<id>[0-9]+)/', PWJS_DjangoProject.uczniowie.views.delete_student),
    url(r'^student/edit/(?P<id>[0-9]+)/', PWJS_DjangoProject.uczniowie.views.edit_student)
]