from django.contrib.auth.models import User
from django.db import models

from utils import TimestampMixin, UserStampedMixin


# Create your models here.

class TravelerRecord(TimestampMixin, UserStampedMixin, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField('First Name', max_length=50)
    middle_name = models.CharField('Middle Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    passport_number = models.CharField('Passport Number', max_length=50)
    phone_number = models.CharField('Phone Number', max_length=15)
    whatsapp_number = models.CharField('Whatsapp Number', max_length=15, null=True)
    email = models.EmailField('Email')

    def __str__(self):
        return self.first_name + " " + self.middle_name


class ProfileImage(TimestampMixin, UserStampedMixin, models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    profile_image = models.ImageField(upload_to='media/profile_image/')

    def __str__(self):
        return str(self.user)
