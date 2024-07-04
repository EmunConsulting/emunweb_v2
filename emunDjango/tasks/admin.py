from django.contrib import admin
from .models import TaskStatus, TaskDescription, Task
from import_export.admin import ImportExportModelAdmin


@admin.register(TaskStatus)
class TaskStatusAdmin(ImportExportModelAdmin):
    list_display = ('id', 'task_status', )
    ordering = ('id', )
    search_fields = ('task_status', )
    list_filter = ('task_status', )


@admin.register(TaskDescription)
class TaskDescriptionAdmin(ImportExportModelAdmin):
    list_display = ('id', 'task_description', )
    ordering = ('id', )


@admin.register(Task)
class TaskAdmin(ImportExportModelAdmin):
    list_display = ('id', 'form', 'task_description', 'facilitator', 'task_status', 'start_date', 'end_date', )
    ordering = ('id', 'start_date', 'end_date', )
    search_fields = ('form', 'facilitator', )
    list_filter = ('form', 'task_description', 'facilitator', 'task_status', 'start_date', 'end_date', )
