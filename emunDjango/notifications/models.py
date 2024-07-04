from django.contrib.auth.models import User
from django.db import models
from travelers.models import TravelerRecord

from utils import TimestampMixin, UserStampedMixin


# Create your models here.

class NotificationStatus(TimestampMixin, UserStampedMixin, models.Model):
    notification_status = models.CharField('Notification Status', max_length=200)

    def __str__(self):
        return self.notification_status


class Notification(TimestampMixin, UserStampedMixin, models.Model):
    traveler = models.ForeignKey(TravelerRecord, on_delete=models.PROTECT)
    notification_content = models.TextField()
    notification_date = models.DateField()
    notification_status = models.ForeignKey(NotificationStatus, on_delete=models.PROTECT)

    def __str__(self):
        return self.traveler
