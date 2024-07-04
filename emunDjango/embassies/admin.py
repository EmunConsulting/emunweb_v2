from django.contrib import admin
from .models import Embassy
from import_export.admin import ImportExportModelAdmin


@admin.register(Embassy)
class EmbassyAdmin(ImportExportModelAdmin):
    list_display = ('id', 'embassy_id', 'embassy_name', 'country', 'phone_number', 'email', 'website', )
    ordering = ('embassy_id', )
    search_fields = ('embassy_name', )
    list_filter = ('embassy_id', 'embassy_name', 'country')


