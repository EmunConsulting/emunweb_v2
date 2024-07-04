from django.contrib.auth.models import User, Group
from django.shortcuts import render
from decorators import authentication_required, allowed_users

from travelers.models import TravelerRecord, ProfileImage
from visaapplications.models import VisaApplication
# Create your views here.


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator'])
def general_report(request):

    tra_rec = TravelerRecord.objects.all().count()
    visa_app = VisaApplication.objects.all().count()
    ini = VisaApplication.objects.filter(application_status=1).count()
    ass = VisaApplication.objects.filter(application_status=2).count()
    inp = VisaApplication.objects.filter(application_status=3).count()
    com = VisaApplication.objects.filter(application_status=4).count()
    can = VisaApplication.objects.filter(application_status=5).count()

    return render(request, 'general_report.html', {
        'tra_rec': tra_rec,
        'visa_app': visa_app,
        'ini': ini,
        'ass': ass,
        'inp': inp,
        'com': com,
        'can': can,
    })


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator'])
def account_list(request):

    info = TravelerRecord.objects.all()

    img = ProfileImage.objects.all()

    return render(request, 'account_list.html', {
        'info': info,
        'img': img,
    })


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator'])
def visa_application_list(request):

    info = VisaApplication.objects.all()

    return render(request, 'visa_application_list.html', {
        'info': info,
    })
