from django.contrib import admin
from .models import RefugeeId, FamilyAttestation, BirthCertificate, NationalID, WeddingCertificate, EmbassyDocument, MedicalDocument, OtherDocument


@admin.register(RefugeeId)
class RefugeeIdAdmin(admin.ModelAdmin):
    list_display = ('id', 'traveler', 'refugee_id',)
    ordering = ('id', )
    search_fields = ('traveler', )
    list_filter = ('traveler', )


@admin.register(FamilyAttestation)
class FamilyAttestationAdmin(admin.ModelAdmin):
    list_display = ('id', 'traveler', 'family_attestation',)
    ordering = ('id', )
    search_fields = ('traveler', )
    list_filter = ('traveler', )


@admin.register(BirthCertificate)
class BirthCertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'traveler', 'birth_certificate',)
    ordering = ('id', )
    search_fields = ('traveler', )
    list_filter = ('traveler', )


@admin.register(NationalID)
class NationalIDAdmin(admin.ModelAdmin):
    list_display = ('id', 'traveler', 'national_id',)
    ordering = ('id', )
    search_fields = ('traveler', )
    list_filter = ('traveler', )


@admin.register(WeddingCertificate)
class WeddingCertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'traveler', 'wedding_certificate',)
    ordering = ('id', )
    search_fields = ('traveler', )
    list_filter = ('traveler', )


@admin.register(EmbassyDocument)
class EmbassyDocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'traveler', 'embassy_document',)
    ordering = ('id', )
    search_fields = ('traveler', )
    list_filter = ('traveler', )


@admin.register(MedicalDocument)
class MedicalDocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'traveler', 'medical_document',)
    ordering = ('id', )
    search_fields = ('traveler', )
    list_filter = ('traveler', )


@admin.register(OtherDocument)
class OtherDocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'traveler', 'other_document',)
    ordering = ('id', )
    search_fields = ('traveler', )
    list_filter = ('traveler', )

