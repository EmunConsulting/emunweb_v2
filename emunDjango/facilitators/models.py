from django.contrib.auth.models import User
from django.db import models

from utils import TimestampMixin, UserStampedMixin


# Create your models here.

class Role(TimestampMixin, UserStampedMixin, models.Model):
    role = models.CharField('Role', max_length=20)

    def __str__(self):
        return self.role


class Account(TimestampMixin, UserStampedMixin, models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, null=True)
    role = models.OneToOneField(Role, on_delete=models.PROTECT, null=True)
    airtel_number = models.CharField('Airtel No', max_length=15)
    mtn_number = models.CharField('MTN No', max_length=15)

    def __str__(self):
        return str(self.user)
