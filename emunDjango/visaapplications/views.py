from django.core.exceptions import ObjectDoesNotExist

from decorators import authentication_required, allowed_users
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import VisaApplication, ApplicantPersonalData, ApplicantTravelDocument, ApplicantHomeAddress, TravelInformation, Reference
from travelers.models import TravelerRecord
# Create your views here.


@authentication_required
@allowed_users(allowed_roles=['admin', 'traveler'])
def visa_application(request):
    if request.method == "POST":
        new_application = VisaApplication.objects.create(application_owner=request.user)
        return redirect(reverse('applicant_personal_data', kwargs={'application_number': new_application.application_number}))

    return render(request, 'visa_application.html')


@authentication_required
@allowed_users(allowed_roles=['admin', 'traveler'])
def end_of_form(request):

    return render(request, 'end_of_form.html')


@authentication_required
@allowed_users(allowed_roles=['admin', 'traveler'])
def applicant_personal_data(request, application_number):
    traveler = TravelerRecord.objects.get(user=request.user)
    if request.method == "POST":
        application = VisaApplication.objects.get(application_number=application_number)
        if application.application_owner != request.user:
            return redirect('home')  # or some error page

        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        date_of_birth = request.POST['date_of_birth']
        month_of_birth = request.POST['month_of_birth']
        year_of_birth = request.POST['year_of_birth']
        place_of_birth = request.POST['place_of_birth']
        country_of_birth = request.POST['country_of_birth']
        current_nationality = request.POST['current_nationality']
        nationality_at_birth = request.POST['nationality_at_birth']
        sex = request.POST['sex']
        marital_status = request.POST['marital_status']
        refugee_id = request.POST['refugee_id']
        current_occupation = request.POST['current_occupation']

        new_rec = ApplicantPersonalData(
            application_number=application,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            month_of_birth=month_of_birth,
            year_of_birth=year_of_birth,
            place_of_birth=place_of_birth,
            country_of_birth=country_of_birth,
            current_nationality=current_nationality,
            nationality_at_birth=nationality_at_birth,
            sex=sex,
            marital_status=marital_status,
            refugee_id=refugee_id,
            current_occupation=current_occupation,
        )
        new_rec.save()
        return redirect('applicant_travel_document', application_number)

    return render(request, 'applicant_personal_data.html', {
        'application_number': application_number,
        'sex': ApplicantPersonalData.GENDER_CHOICES,
        'traveler': traveler,
    })


@authentication_required
@allowed_users(allowed_roles=['admin', 'traveler'])
def update_applicant_personal_data(request, application_number):

    try:
        # Retrieve the VisaApplication instance
        visa_app = VisaApplication.objects.get(id=application_number)
    except VisaApplication.DoesNotExist:
        raise ObjectDoesNotExist(f"VisaApplication with id {application_number} does not exist")

    # Retrieve or create the ApplicantPersonalData record
    rec, created = ApplicantPersonalData.objects.get_or_create(application_number=visa_app)

    try:
        traveler = TravelerRecord.objects.get(user=request.user)
    except TravelerRecord.DoesNotExist:
        raise ObjectDoesNotExist(f"TravelerRecord for user {request.user} does not exist")
    if request.method == "POST":

        rec.first_name = request.POST['first_name']
        rec.middle_name = request.POST['middle_name']
        rec.last_name = request.POST['last_name']
        rec.date_of_birth = request.POST['date_of_birth']
        rec.month_of_birth = request.POST['month_of_birth']
        rec.year_of_birth = request.POST['year_of_birth']
        rec.place_of_birth = request.POST['place_of_birth']
        rec.country_of_birth = request.POST['country_of_birth']
        rec.current_nationality = request.POST['current_nationality']
        rec.nationality_at_birth = request.POST['nationality_at_birth']
        rec.sex = request.POST['sex']
        rec.marital_status = request.POST['marital_status']
        rec.refugee_id = request.POST['refugee_id']
        rec.current_occupation = request.POST['current_occupation']

        rec.save()
        return redirect('list_my_applications')

    return render(request, 'update_applicant_personal_data.html', {
        'sex': ApplicantPersonalData.GENDER_CHOICES,
        'rec': rec,
        'traveler': traveler,
    })


@authentication_required
@allowed_users(allowed_roles=['admin', 'traveler'])
def applicant_travel_document(request, application_number):
    traveler = TravelerRecord.objects.get(user=request.user)
    if request.method == "POST":
        application = VisaApplication.objects.get(application_number=application_number)
        if application.application_owner != request.user:
            return redirect('home')  # or some error page

        document_type = request.POST['document_type']
        document_number = request.POST['document_number']
        date_of_issue = request.POST['date_of_issue']
        valid_until = request.POST['valid_until']
        issued_by = request.POST['issued_by']
        issuing_country = request.POST['issuing_country']

        new_rec = ApplicantTravelDocument(
            application_number=application,
            document_type=document_type,
            document_number=document_number,
            date_of_issue=date_of_issue,
            valid_until=valid_until,
            issued_by=issued_by,
            issuing_country=issuing_country,
        )
        new_rec.save()
        return redirect('applicant_home_address', application_number)

    return render(request, 'applicant_travel_document.html', {
        'application_number': application_number,
        'traveler': traveler,
    })


@authentication_required
@allowed_users(allowed_roles=['admin', 'traveler'])
def update_applicant_travel_document(request, application_number):

    try:
        # Retrieve the VisaApplication instance
        visa_app = VisaApplication.objects.get(id=application_number)
    except VisaApplication.DoesNotExist:
        raise ObjectDoesNotExist(f"VisaApplication with id {application_number} does not exist")

    # Retrieve or create the ApplicantTravelDocument record
    rec, created = ApplicantTravelDocument.objects.get_or_create(application_number=visa_app)

    try:
        traveler = TravelerRecord.objects.get(user=request.user)
    except TravelerRecord.DoesNotExist:
        raise ObjectDoesNotExist(f"TravelerRecord for user {request.user} does not exist")
    if request.method == "POST":

        rec.document_type = request.POST['document_type']
        rec.document_number = request.POST['document_number']
        rec.date_of_issue = request.POST['date_of_issue']
        rec.valid_until = request.POST['valid_until']
        rec.issued_by = request.POST['issued_by']
        rec.issuing_country = request.POST['issuing_country']

        rec.save()
        return redirect('list_my_applications')

    return render(request, 'update_applicant_travel_document.html', {
        'rec': rec,
        'traveler': traveler,
    })


@authentication_required
@allowed_users(allowed_roles=['admin', 'traveler'])
def applicant_home_address(request, application_number):
    traveler = TravelerRecord.objects.get(user=request.user)
    if request.method == "POST":
        application = VisaApplication.objects.get(application_number=application_number)
        if application.application_owner != request.user:
            return redirect('home')  # or some error page

        street = request.POST['street']
        city = request.POST['city']
        country = request.POST['country']
        phone_number = request.POST['phone_number']
        whatsapp_number = request.POST['whatsapp_number']
        email = request.POST['email']

        new_rec = ApplicantHomeAddress(
            application_number=application,
            street=street,
            city=city,
            country=country,
            phone_number=phone_number,
            whatsapp_number=whatsapp_number,
            email=email,
        )
        new_rec.save()
        return redirect('travel_information', application_number)

    return render(request, 'applicant_home_address.html', {
        'application_number': application_number,
        'traveler': traveler,
    })


@authentication_required
@allowed_users(allowed_roles=['admin', 'traveler'])
def update_applicant_home_address(request, application_number):

    try:
        # Retrieve the VisaApplication instance
        visa_app = VisaApplication.objects.get(id=application_number)
    except VisaApplication.DoesNotExist:
        raise ObjectDoesNotExist(f"VisaApplication with id {application_number} does not exist")

    # Retrieve or create the HomeAddress record
    rec, created = ApplicantHomeAddress.objects.get_or_create(application_number=visa_app)

    try:
        traveler = TravelerRecord.objects.get(user=request.user)
    except TravelerRecord.DoesNotExist:
        raise ObjectDoesNotExist(f"TravelerRecord for user {request.user} does not exist")

    if request.method == "POST":

        rec.street = request.POST['street']
        rec.city = request.POST['city']
        rec.country = request.POST['country']
        rec.phone_number = request.POST['phone_number']
        rec.whatsapp_number = request.POST['whatsapp_number']
        rec.email = request.POST['email']

        rec.save()
        return redirect('list_my_applications')

    return render(request, 'update_applicant_home_address.html', {
        'rec': rec,
        'traveler': traveler,
    })


@authentication_required
@allowed_users(allowed_roles=['admin', 'traveler'])
def travel_information(request, application_number):
    traveler = TravelerRecord.objects.get(user=request.user)
    if request.method == "POST":
        application = VisaApplication.objects.get(application_number=application_number)
        if application.application_owner != request.user:
            return redirect('home')  # or some error page

        visa_type = request.POST['visa_type']
        main_purpose_of_journey = request.POST['main_purpose_of_journey']
        member_state_of_destination = request.POST['member_state_of_destination']
        member_state_of_first_entry = request.POST['member_state_of_first_entry']
        number_of_entries_required = request.POST['number_of_entries_required']

        new_rec = TravelInformation(
            application_number=application,
            visa_type=visa_type,
            main_purpose_of_journey=main_purpose_of_journey,
            member_state_of_destination=member_state_of_destination,
            member_state_of_first_entry=member_state_of_first_entry,
            number_of_entries_required=number_of_entries_required,
        )
        new_rec.save()
        return redirect('reference', application_number)

    return render(request, 'travel_information.html', {
        'application_number': application_number,
        'traveler': traveler,
    })


@authentication_required
@allowed_users(allowed_roles=['admin', 'traveler'])
def update_travel_information(request, application_number):

    try:
        # Retrieve the VisaApplication instance
        visa_app = VisaApplication.objects.get(id=application_number)
    except VisaApplication.DoesNotExist:
        raise ObjectDoesNotExist(f"VisaApplication with id {application_number} does not exist")

    # Retrieve or create the TravelInformation record
    rec, created = TravelInformation.objects.get_or_create(application_number=visa_app)

    try:
        traveler = TravelerRecord.objects.get(user=request.user)
    except TravelerRecord.DoesNotExist:
        raise ObjectDoesNotExist(f"TravelerRecord for user {request.user} does not exist")

    if request.method == "POST":

        rec.visa_type = request.POST['visa_type']
        rec.main_purpose_of_journey = request.POST['main_purpose_of_journey']
        rec.member_state_of_destination = request.POST['member_state_of_destination']
        rec.member_state_of_first_entry = request.POST['member_state_of_first_entry']
        rec.number_of_entries_required = request.POST['number_of_entries_required']

        rec.save()
        return redirect('list_my_applications')

    return render(request, 'update_travel_information.html', {
        'rec': rec,
        'traveler': traveler,
    })


@authentication_required
@allowed_users(allowed_roles=['admin', 'traveler'])
def reference(request, application_number):
    traveler = TravelerRecord.objects.get(user=request.user)
    if request.method == "POST":
        application = VisaApplication.objects.get(application_number=application_number)
        if application.application_owner != request.user:
            return redirect('home')  # or some error page

        type = request.POST['type']
        has_national_id = request.POST.get('has_national_id', '')
        national_registration_number = request.POST.get('national_registration_number', '')
        identity_document_number = request.POST.get('identity_document_number', '')
        surname = request.POST.get('surname', '')
        first_name = request.POST.get('first_name', '')
        gender = request.POST.get('gender', '')
        street = request.POST['street']
        postal_code = request.POST['postal_code']
        city = request.POST['city']
        country = request.POST['country']
        telephone_number = request.POST['telephone_number']
        mobile_number = request.POST['mobile_number']
        email = request.POST['email']

        new_rec = Reference(
            application_number=application,
            type=type,
            has_national_id=has_national_id,
            national_registration_number=national_registration_number,
            identity_document_number=identity_document_number,
            surname=surname,
            first_name=first_name,
            gender=gender,
            street=street,
            postal_code=postal_code,
            city=city,
            country=country,
            telephone_number=telephone_number,
            mobile_number=mobile_number,
            email=email,
        )

        new_rec.save()
        return redirect('end_of_form')

    return render(request, 'reference.html', {
        'application_number': application_number,
        'gender': ApplicantPersonalData.GENDER_CHOICES,
        'has_national_id': Reference.HNID_CHOICES,
        'type': Reference.TYPE_CHOICES,
        'traveler': traveler,
    })


@authentication_required
@allowed_users(allowed_roles=['admin', 'traveler'])
def update_reference(request, application_number):

    try:
        # Retrieve the VisaApplication instance
        visa_app = VisaApplication.objects.get(id=application_number)
    except VisaApplication.DoesNotExist:
        raise ObjectDoesNotExist(f"VisaApplication with id {application_number} does not exist")

    # Retrieve or create the Reference record
    rec, created = Reference.objects.get_or_create(application_number=visa_app)

    try:
        traveler = TravelerRecord.objects.get(user=request.user)
    except TravelerRecord.DoesNotExist:
        raise ObjectDoesNotExist(f"TravelerRecord for user {request.user} does not exist")

    if request.method == "POST":
        rec.type = request.POST.get('type', '')
        rec.has_national_id = request.POST.get('has_national_id', '')
        rec.national_registration_number = request.POST.get('national_registration_number', '')
        rec.identity_document_number = request.POST.get('identity_document_number', '')
        rec.surname = request.POST.get('surname', '')
        rec.first_name = request.POST.get('first_name', '')
        rec.gender = request.POST.get('gender', '')
        rec.street = request.POST.get('street', '')
        rec.postal_code = request.POST.get('postal_code', '')
        rec.city = request.POST.get('city', '')
        rec.country = request.POST.get('country', '')
        rec.telephone_number = request.POST.get('telephone_number', '')
        rec.mobile_number = request.POST.get('mobile_number', '')
        rec.email = request.POST.get('email', '')

        rec.save()
        return redirect('list_my_applications')

    return render(request, 'update_reference.html', {
        'rec': rec,
        'gender': ApplicantPersonalData.GENDER_CHOICES,
        'has_national_id': Reference.HNID_CHOICES,
        'type': Reference.TYPE_CHOICES,
        'traveler': traveler,
    })
