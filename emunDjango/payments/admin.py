from django.contrib import admin
from .models import PaymentStatus, PaymentMethod, Payment
from import_export.admin import ImportExportModelAdmin


@admin.register(PaymentStatus)
class PaymentStatusAdmin(ImportExportModelAdmin):
    list_display = ('id', 'payment_status', )
    ordering = ('id', )
    search_fields = ('payment_status', )
    list_filter = ('payment_status', )


@admin.register(PaymentMethod)
class PaymentMethodAdmin(ImportExportModelAdmin):
    list_display = ('id', 'payment_method', )
    ordering = ('id', )
    search_fields = ('payment_method', )
    list_filter = ('payment_method', )


@admin.register(Payment)
class PaymentAdmin(ImportExportModelAdmin):
    list_display = ('id', 'payment_date', 'payment_id', 'traveler', 'payment_reason', 'payable_amount', 'paid_amount', 'payment_method', 'remaining_amount', 'payment_status', )
    ordering = ('id', 'payment_date', )
    search_fields = ('traveler', )
    list_filter = ('payment_date', 'traveler', 'payment_method', 'payment_status', )
