# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Nauczyciel, Przedmiot, Uczen

# Register your models here.
admin.site.register(Nauczyciel)
admin.site.register(Przedmiot)
admin.site.register(Uczen)