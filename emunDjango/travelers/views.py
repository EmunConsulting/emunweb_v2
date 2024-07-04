from decorators import paginate, authentication_required, allowed_users
from utils import get_records_per_page

from datetime import date, datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib import messages

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count

from .models import TravelerRecord, ProfileImage
from visaapplications.models import VisaApplication, ApplicantPersonalData, ApplicantTravelDocument, ApplicantHomeAddress
from visaapplications.models import TravelInformation, Reference


# Create your views here.


@authentication_required
@allowed_users(allowed_roles=['admin', 'traveler'])
def profile_info(request):

    # info = TravelerRecord.objects.get(user=request.user)

    try:
        info = TravelerRecord.objects.get(user=request.user)
    except TravelerRecord.DoesNotExist:
        info = None

    visa_app = VisaApplication.objects.filter(application_owner=request.user.id)
    per_data = ApplicantPersonalData.objects.filter(application_number__application_owner=request.user)
    tra_doc = ApplicantTravelDocument.objects.filter(application_number__application_owner=request.user)
    hom_add = ApplicantHomeAddress.objects.filter(application_number__application_owner=request.user)
    tra_inf = TravelInformation.objects.filter(application_number__application_owner=request.user)
    ref = Reference.objects.filter(application_number__application_owner=request.user)

    return render(request, 'profile_info.html', {
        'info': info,
        'visa_app': visa_app,
        'per_data': per_data,
        'tra_doc': tra_doc,
        'hom_add': hom_add,
        'tra_inf': tra_inf,
        'ref': ref,
    })


@authentication_required
@allowed_users(allowed_roles=['admin', 'traveler'])
def list_my_applications(request):
    visa_app = VisaApplication.objects.filter(application_owner=request.user.id)

    return render(request, 'list_my_applications.html', {
        'visa_app': visa_app,
    })


@authentication_required
@allowed_users(allowed_roles=['admin', 'traveler', 'moderator', 'facilitator'])
def compiled_application(request, pk):
    visa_app = get_object_or_404(VisaApplication, id=pk)

    try:
        per_data = ApplicantPersonalData.objects.get(application_number=visa_app.id)
    except ApplicantPersonalData.DoesNotExist:
        per_data = None

    try:
        tra_doc = ApplicantTravelDocument.objects.get(application_number=visa_app.id)
    except ApplicantTravelDocument.DoesNotExist:
        tra_doc = None

    try:
        hom_add = ApplicantHomeAddress.objects.get(application_number=visa_app.id)
    except ApplicantHomeAddress.DoesNotExist:
        hom_add = None

    try:
        tra_inf = TravelInformation.objects.get(application_number=visa_app.id)
    except TravelInformation.DoesNotExist:
        tra_inf = None

    try:
        ref = Reference.objects.get(application_number=visa_app.id)
    except Reference.DoesNotExist:
        ref = None

    return render(request, 'compiled_application.html', {
        'visa_app': visa_app,
        'per_data': per_data,
        'tra_doc': tra_doc,
        'hom_add': hom_add,
        'tra_inf': tra_inf,
        'ref': ref,
    })



