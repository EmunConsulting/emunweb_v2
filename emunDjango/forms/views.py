from decorators import paginate, authentication_required, allowed_users
from utils import get_records_per_page

from datetime import date, datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib import messages

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count

from .models import Form, SubmittedForm

# Create your views here.


@authentication_required
@allowed_users(allowed_roles=['admin', 'traveler'])
@paginate(template_name='forms.html')
def form(request):

    forms = Form.objects.all()

    records_per_page = get_records_per_page(request)
    paginator = Paginator(forms, records_per_page)

    return {'data': paginator.page(1),
            'paginator': paginator,
            }


@authentication_required
@allowed_users(allowed_roles=['admin', 'traveler'])
def submit_form(request):

    if request.method == "POST":
        user = request.user
        attachment = request.POST['attachment']
        additional_note = request.POST['additional_note']

        new_rec = SubmittedForm(
            user=user,
            attachment=attachment,
            additional_note=additional_note,

        )
        new_rec.save()
        messages.success(request, "Record Added")

        return redirect('submit_form')

    return render(request, 'submit_form.html', {})

