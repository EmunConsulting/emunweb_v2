from django.contrib import admin
from .models import Form, SubmittedForm
from import_export.admin import ImportExportModelAdmin


@admin.register(Form)
class FormAdmin(ImportExportModelAdmin):
    list_display = ('id', 'form_id', 'form_name', 'description', 'embassy', )
    ordering = ('id', )
    search_fields = ('form_name', 'embassy', )
    list_filter = ('embassy', )


@admin.register(SubmittedForm)
class SubmittedFormAdmin(ImportExportModelAdmin):
    list_display = ('id', 'user', 'attachment', 'additional_note', )
    ordering = ('id', )
    search_fields = ('user', )
