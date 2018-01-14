"""PWJS_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from PWJS_DjangoProject import index
from PWJS_Django import views
urlpatterns = [
    url(r'^$', index.hello),
    url(r'^admin/', admin.site.urls),
    url(r'^lectures/$', views.lectures),
    url(r'^lecture/(?P<id>[0-9]+)/', views.lecture),
    url(r'^lecture/delete/(?P<id>[0-9]+)/', views.delete_lecture),
    url(r'^lecture/edit/(?P<id>[0-9]+)/', views.edit_lecture),
    url(r'^lecture/sign_student/(?P<id>[0-9]+)/', views.sign_student),
    url(r'^students/', views.students),
    url(r'^student/(?P<id>[0-9]+)/', views.student),
    url(r'^student/delete/(?P<id>[0-9]+)/', views.delete_student),
    url(r'^student/edit/(?P<id>[0-9]+)/', views.edit_student),
    url(r'^teachers/', views.teachers),
    url(r'^teacher/(?P<id>[0-9]+)/', views.teacher),
    url(r'^teacher/delete/(?P<id>[0-9]+)/', views.delete_teacher),
    url(r'^teacher/edit/(?P<id>[0-9]+)/', views.edit_teacher)
]
