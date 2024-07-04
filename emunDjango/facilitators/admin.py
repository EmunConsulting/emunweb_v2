from django.contrib import admin
from .models import Role, Account

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'role', )
    ordering = ('id', )
    search_fields = ('role', )
    list_filter = ('role', )


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'role', 'airtel_number', 'mtn_number', )
    ordering = ('id', )
    search_fields = ('user', )
    list_filter = ('user', )
