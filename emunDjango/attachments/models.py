from django.contrib.auth.models import User
from utils import custom_upload_to

from django.db import models
from travelers.models import TravelerRecord

from utils import TimestampMixin, UserStampedMixin


# Create your models here.
class RefugeeId(TimestampMixin, UserStampedMixin, models.Model):
    traveler = models.ForeignKey(TravelerRecord, on_delete=models.PROTECT)
    refugee_id = models.ImageField(upload_to=custom_upload_to)

    def __str__(self):
        return str(self.traveler)


class FamilyAttestation(TimestampMixin, UserStampedMixin, models.Model):
    traveler = models.ForeignKey(TravelerRecord, on_delete=models.PROTECT)
    family_attestation = models.ImageField(upload_to=custom_upload_to)

    def __str__(self):
        return str(self.traveler)


class BirthCertificate(TimestampMixin, UserStampedMixin, models.Model):
    traveler = models.ForeignKey(TravelerRecord, on_delete=models.PROTECT)
    birth_certificate = models.ImageField(upload_to=custom_upload_to)

    def __str__(self):
        return str(self.traveler)


class NationalID(TimestampMixin, UserStampedMixin, models.Model):
    traveler = models.ForeignKey(TravelerRecord, on_delete=models.PROTECT)
    national_id = models.ImageField(upload_to=custom_upload_to)

    def __str__(self):
        return str(self.traveler)


class WeddingCertificate(TimestampMixin, UserStampedMixin, models.Model):
    traveler = models.ForeignKey(TravelerRecord, on_delete=models.PROTECT)
    wedding_certificate = models.ImageField(upload_to=custom_upload_to)

    def __str__(self):
        return str(self.traveler)


class EmbassyDocument(TimestampMixin, UserStampedMixin, models.Model):
    traveler = models.ForeignKey(TravelerRecord, on_delete=models.PROTECT)
    embassy_document = models.ImageField(upload_to=custom_upload_to)

    def __str__(self):
        return str(self.traveler)


class MedicalDocument(TimestampMixin, UserStampedMixin, models.Model):
    traveler = models.ForeignKey(TravelerRecord, on_delete=models.PROTECT)
    medical_document = models.ImageField(upload_to=custom_upload_to)

    def __str__(self):
        return str(self.traveler)


class OtherDocument(TimestampMixin, UserStampedMixin, models.Model):
    traveler = models.ForeignKey(TravelerRecord, on_delete=models.PROTECT)
    other_document = models.ImageField(upload_to=custom_upload_to)

    def __str__(self):
        return str(self.traveler)
