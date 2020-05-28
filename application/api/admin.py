from django.contrib import admin

# Register your models here.
from api.models import Person, Task

class TasksAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'person']


class PersonAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Task, TasksAdmin)
admin.site.register(Person, PersonAdmin)