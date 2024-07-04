from django.contrib.auth.models import User
from django.db import models

from utils import TimestampMixin, UserStampedMixin


# Create your models here.

class Embassy(TimestampMixin, UserStampedMixin, models.Model):
    embassy_id = models.CharField('Embassy ID', max_length=15)
    embassy_name = models.CharField('Embassy Name', max_length=100)
    country = models.CharField('Country', max_length=100)
    phone_number = models.CharField('Phone Number', max_length=15, blank=True)
    email = models.EmailField('Email', blank=True)
    website = models.CharField('Website', max_length=200)

    def __str__(self):
        return self.embassy_name
