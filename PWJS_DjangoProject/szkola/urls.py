import PWJS_DjangoProject.szkola.views
from django.conf.urls import url
urlpatterns = [
    url(r'^lectures/$', PWJS_DjangoProject.szkola.views.lectures),
    url(r'^lectures/lecture/(?P<id>[0-9]+)/', PWJS_DjangoProject.szkola.views.lecture)
]