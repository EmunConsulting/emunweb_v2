import os
from django.contrib.auth.models import User
from django.db import models
from embassies.models import Embassy

from utils import TimestampMixin, UserStampedMixin


# Create your models here.

class Form(TimestampMixin, UserStampedMixin, models.Model):
    form_id = models.CharField('Form ID', max_length=15)
    form_name = models.FileField(upload_to='uploaded_forms/')
    description = models.TextField('Description')
    embassy = models.ForeignKey(Embassy, on_delete=models.PROTECT)

    def __str__(self):
        return os.path.basename(self.form_name.name)


class SubmittedForm(TimestampMixin, UserStampedMixin, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    attachment = models.FileField(upload_to='submitted_forms/')
    additional_note = models.TextField('Additional Notes')

    def __str__(self):
        return os.path.basename(self.attachment.name)
