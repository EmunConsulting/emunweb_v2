from django.contrib import admin
from .models import NotificationStatus, Notification
from import_export.admin import ImportExportModelAdmin


@admin.register(NotificationStatus)
class NotificationStatusAdmin(ImportExportModelAdmin):
    list_display = ('id', 'notification_status', )
    ordering = ('id', )
    search_fields = ('notification_status', )
    list_filter = ('notification_status', )


@admin.register(Notification)
class NotificationAdmin(ImportExportModelAdmin):
    list_display = ('id', 'traveler', 'notification_content', 'notification_date', 'notification_status', )
    ordering = ('id', )
    search_fields = ('traveler', )
    list_filter = ('traveler', 'notification_date', 'notification_status', )
