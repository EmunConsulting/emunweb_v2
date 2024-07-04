from django.contrib.auth.models import User
from django.db import models
from forms.models import Form

from utils import TimestampMixin, UserStampedMixin


# Create your models here.

class TaskDescription(TimestampMixin, UserStampedMixin, models.Model):
    task_description = models.CharField('Task Description', max_length=200)

    def __str__(self):
        return self.task_description


class TaskStatus(TimestampMixin, UserStampedMixin, models.Model):
    task_status = models.CharField('Task Status', max_length=100)

    def __str__(self):
        return self.task_status


class Task(TimestampMixin, UserStampedMixin, models.Model):
    form = models.ForeignKey(Form, on_delete=models.PROTECT)
    task_description = models.ForeignKey(TaskDescription, on_delete=models.PROTECT)
    facilitator = models.ForeignKey(User, on_delete=models.PROTECT)
    task_status = models.ForeignKey(TaskStatus, on_delete=models.PROTECT)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.facilitator
