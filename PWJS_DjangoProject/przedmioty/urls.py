import PWJS_DjangoProject.przedmioty.views
from django.conf.urls import url
urlpatterns = [
    url(r'^$', PWJS_DjangoProject.przedmioty.views.lectures),
    url(r'^lecture/(?P<id>[0-9]+)/', PWJS_DjangoProject.przedmioty.views.lecture),
    url(r'^lecture/delete/(?P<id>[0-9]+)/', PWJS_DjangoProject.przedmioty.views.delete_lecture),
    url(r'^lecture/edit/(?P<id>[0-9]+)/', PWJS_DjangoProject.przedmioty.views.edit_lecture),
    url(r'^lecture/sign_student/(?P<id>[0-9]+)/', PWJS_DjangoProject.przedmioty.views.sign_student)
]