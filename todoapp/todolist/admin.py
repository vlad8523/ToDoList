from django.contrib import admin

# Register your models here.

from .models import Task, Importance

admin.site.register(Task)
admin.site.register(Importance)