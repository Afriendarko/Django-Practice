from django.contrib import admin

# Register your models here.
from demoapp.models import Musician1
from demoapp.models import venue


admin.site.register(Musician1)
admin.site.register(venue)