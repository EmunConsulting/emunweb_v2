import os

from django.db import models
from django.contrib.auth.models import User


# Adds the following fields to model
class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


# Adds the following fields to model
class UserStampedMixin(models.Model):
    registered_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='%(class)s_registered_by', null=True, editable=False,)
    last_updated_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, related_name='%(class)s_last_updated_by', editable=False)

    class Meta:
        abstract = True


# Common part of pagination that starts with default number of rows per page and can switch to user selected amount
def get_records_per_page(request):
    from constants import RECORDS_PER_PAGE_DEFAULT

    records_per_page = request.GET.get('recordsPerPage', RECORDS_PER_PAGE_DEFAULT)
    try:
        records_per_page = int(records_per_page)
    except ValueError:
        records_per_page = RECORDS_PER_PAGE_DEFAULT
    return records_per_page


def custom_upload_to(instance, filename):
    model_name = instance.__class__.__name__
    user_id = instance.traveler.user.id
    base, extension = os.path.splitext(filename)
    new_filename = f"{user_id}_{model_name.lower()}_{base}{extension}"
    return os.path.join('media/uploaded_attachments', new_filename)

