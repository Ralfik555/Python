from django.contrib import admin

# Register your models here.

from .models import Employee, Event, EventHandler, Skills

admin.site.register(Employee)
admin.site.register(Event)
admin.site.register(EventHandler)
admin.site.register(Skills)