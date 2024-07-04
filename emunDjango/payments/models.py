from django.contrib.auth.models import User
from django.db import models
from travelers.models import TravelerRecord

from utils import TimestampMixin, UserStampedMixin


# Create your models here.

class PaymentStatus(TimestampMixin, UserStampedMixin, models.Model):
    payment_status = models.CharField('Payment Status', max_length=100)

    def __str__(self):
        return self.payment_status


class PaymentMethod(TimestampMixin, UserStampedMixin, models.Model):
    payment_method = models.CharField('Payment Method', max_length=100)

    def __str__(self):
        return self.payment_method


class Payment(TimestampMixin, UserStampedMixin, models.Model):
    payment_date = models.DateField()
    payment_id = models.CharField('Payment ID', max_length=100)
    traveler = models.ForeignKey(TravelerRecord, on_delete=models.PROTECT)
    payment_reason = models.TextField()
    payable_amount = models.PositiveIntegerField()
    paid_amount = models.PositiveIntegerField()
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.PROTECT)
    remaining_amount = models.PositiveIntegerField()
    payment_status = models.ForeignKey(PaymentStatus, on_delete=models.PROTECT)

    def __str__(self):
        return self.traveler
