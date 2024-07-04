import uuid
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import VisaApplication


def generate_application_number():
    prefix = "AP-"
    unique_number = uuid.uuid4().hex[:6].upper()  # Generate a unique 6-character string
    return f"{prefix}{unique_number}"


@receiver(pre_save, sender=VisaApplication)
def set_application_number(sender, instance, **kwargs):
    if not instance.application_number:
        instance.application_number = generate_application_number()
