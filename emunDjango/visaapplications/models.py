from django.contrib.auth.models import User
from django.db import models
import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from utils import TimestampMixin, UserStampedMixin


class VisaApplication(TimestampMixin, UserStampedMixin, models.Model):

    STATUS_CHOICES = [
        ('1', 'Initiated'),
        ('2', 'Assigned'),
        ('3', 'In Progress'),
        ('4', 'Completed'),
        ('5', 'Cancelled'),
    ]

    # Metadata
    application_owner = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    application_number = models.CharField(max_length=10, unique=True, blank=True)
    date_submitted = models.DateTimeField(auto_now_add=True)
    application_status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='1',)
    assigned_officer = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name="person_assigned")
    officer_notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.application_number


class ApplicantPersonalData(TimestampMixin, UserStampedMixin, models.Model):

    GENDER_CHOICES = [
        ('1', 'ተባ/M'),
        ('2', 'ኣን/F'),
    ]

    application_number = models.ForeignKey(VisaApplication, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(31)])
    month_of_birth = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    year_of_birth = models.PositiveIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(datetime.date.today().year)])
    place_of_birth = models.CharField(max_length=100)
    country_of_birth = models.CharField(max_length=100)
    current_nationality = models.CharField(max_length=100)
    nationality_at_birth = models.CharField(max_length=100)
    sex = models.CharField(max_length=1, choices=GENDER_CHOICES,)
    marital_status = models.CharField(max_length=20)
    refugee_id = models.CharField(max_length=100, null=True, blank=True)
    current_occupation = models.CharField(max_length=100)


class ApplicantTravelDocument(TimestampMixin, UserStampedMixin, models.Model):
    application_number = models.ForeignKey(VisaApplication, on_delete=models.CASCADE)
    document_type = models.CharField(max_length=100,)
    document_number = models.CharField(max_length=100)
    date_of_issue = models.DateField()
    valid_until = models.DateField()
    issued_by = models.CharField(max_length=100)
    issuing_country = models.CharField(max_length=100)


class ApplicantHomeAddress(TimestampMixin, UserStampedMixin, models.Model):
    application_number = models.ForeignKey(VisaApplication, on_delete=models.CASCADE)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    whatsapp_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField()


class TravelInformation(TimestampMixin, UserStampedMixin, models.Model):
    application_number = models.ForeignKey(VisaApplication, on_delete=models.CASCADE)
    visa_type = models.CharField(max_length=100)
    main_purpose_of_journey = models.CharField(max_length=200)
    member_state_of_destination = models.CharField(max_length=100)
    member_state_of_first_entry = models.CharField(max_length=100)
    number_of_entries_required = models.CharField(max_length=100)


class Reference(TimestampMixin, UserStampedMixin, models.Model):
    GENDER_CHOICES = [
        ('1', 'ተባ/M'),
        ('2', 'ኣን/F'),
    ]

    TYPE_CHOICES = [
        ('1', 'ሰብ/Person'),
        ('2', 'ሆቴል/Hotel'),
    ]

    HNID_CHOICES = [
        ('1', 'እወ/True'),
        ('2', 'ኣይፋል/False'),
    ]

    application_number = models.ForeignKey(VisaApplication, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    has_national_id = models.CharField(max_length=10, choices=HNID_CHOICES)
    national_registration_number = models.CharField(max_length=100, null=True, blank=True)
    identity_document_number = models.CharField(max_length=100, null=True, blank=True)
    surname = models.CharField(max_length=100, blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    telephone_number = models.CharField(max_length=15, blank=True)
    mobile_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField()

