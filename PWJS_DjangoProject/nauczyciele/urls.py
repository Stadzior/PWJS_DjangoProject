import PWJS_DjangoProject.nauczyciele.views
from django.conf.urls import url
urlpatterns = [
    url(r'^$', PWJS_DjangoProject.nauczyciele.views.teachers),
    url(r'^teacher/(?P<id>[0-9]+)/', PWJS_DjangoProject.nauczyciele.views.teacher),
    url(r'^teacher/delete/(?P<id>[0-9]+)/', PWJS_DjangoProject.nauczyciele.views.delete_teacher),
    url(r'^teacher/edit/(?P<id>[0-9]+)/', PWJS_DjangoProject.nauczyciele.views.edit_teacher)
]