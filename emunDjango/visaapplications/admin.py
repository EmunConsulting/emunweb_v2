from django.contrib import admin
from .models import VisaApplication, ApplicantPersonalData, ApplicantTravelDocument, ApplicantHomeAddress, TravelInformation, Reference


# Register your models here.
@admin.register(VisaApplication)
class VisaApplicationAdmin(admin.ModelAdmin):
    list_display = ('application_owner', 'application_number', 'date_submitted', 'application_status', 'assigned_officer', 'officer_notes', )
    ordering = ('date_submitted', )
    search_fields = ('application_owner', 'application_status', 'assigned_officer', )
    list_filter = ('application_owner', 'application_status', 'assigned_officer', )


@admin.register(ApplicantPersonalData)
class ApplicantPersonalDataAdmin(admin.ModelAdmin):
    list_display = ('application_number', 'first_name', 'middle_name', 'last_name', 'date_of_birth', 'month_of_birth', 'year_of_birth', 'place_of_birth', 'country_of_birth', 'current_nationality', 'nationality_at_birth', 'sex', 'marital_status', 'refugee_id', 'current_occupation', )
    ordering = ('first_name', )
    search_fields = ('first_name', 'middle_name', 'last_name', )


@admin.register(ApplicantTravelDocument)
class ApplicantTravelDocumentAdmin(admin.ModelAdmin):
    list_display = ('application_number', 'document_type', 'document_number', 'date_of_issue', 'valid_until', 'issued_by', 'issuing_country', )
    ordering = ('id', )
    search_fields = ('application_number', )
    list_filter = ('document_type', )


@admin.register(ApplicantHomeAddress)
class ApplicantHomeAddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'application_number', 'street', 'city', 'country', 'phone_number', 'phone_number', 'email', )
    ordering = ('id', )
    search_fields = ('street', 'city', )


@admin.register(TravelInformation)
class TravelInformationAdmin(admin.ModelAdmin):
    list_display = ('application_number', 'visa_type', 'main_purpose_of_journey', 'member_state_of_destination', 'member_state_of_first_entry', 'number_of_entries_required', )
    ordering = ('id', )
    search_fields = ('visa_type', )
    list_filter = ('visa_type',)


@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('application_number', 'type', 'has_national_id', 'national_registration_number', 'identity_document_number', 'surname', 'first_name', 'gender', 'street', 'postal_code', 'city', 'country', 'telephone_number', 'mobile_number', 'email', )
    ordering = ('id', )
    search_fields = ('application_number', )
    list_filter = ('application_number', )
