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
from PWJS_DjangoProject import hello_view

urlpatterns = [
    url(r'^$', hello_view.hello),
    url(r'^admin/', admin.site.urls),
    url(r'^szkola/', include('PWJS_DjangoProject.szkola.urls')),
    url(r'^lectures/', include('PWJS_DjangoProject.przedmioty.urls')),
    url(r'^students/', include('PWJS_DjangoProject.uczniowie.urls')),
    url(r'^teachers/', include('PWJS_DjangoProject.nauczyciele.urls'))
]
