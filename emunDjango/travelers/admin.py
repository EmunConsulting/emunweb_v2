from django.contrib import admin
from .models import TravelerRecord, ProfileImage


@admin.register(TravelerRecord)
class TravelerRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'middle_name', 'last_name', 'passport_number', 'phone_number', 'whatsapp_number', 'email', )
    ordering = ('id', )
    search_fields = ('first_name', 'middle_name', 'last_name', 'passport_number', )


@admin.register(ProfileImage)
class ProfileImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'profile_image', )
    ordering = ('id', )

