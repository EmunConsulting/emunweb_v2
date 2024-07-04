from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.apps import apps
from .models import RefugeeId, FamilyAttestation, BirthCertificate, NationalID, WeddingCertificate, EmbassyDocument, MedicalDocument, OtherDocument
from decorators import authentication_required, allowed_users
from travelers.models import TravelerRecord


# Create your views here.
@authentication_required
@allowed_users(allowed_roles=['admin', 'traveler', 'facilitator'])
def attach(request):

    ref_id = RefugeeId.objects.filter(traveler__user=request.user).count()
    fam_att = FamilyAttestation.objects.filter(traveler__user=request.user.id).count()
    bir_cer = BirthCertificate.objects.filter(traveler__user=request.user.id).count()
    nat_id = NationalID.objects.filter(traveler__user=request.user.id).count()
    wed_cer = WeddingCertificate.objects.filter(traveler__user=request.user.id).count()
    emb_doc = EmbassyDocument.objects.filter(traveler__user=request.user.id).count()
    med_doc = MedicalDocument.objects.filter(traveler__user=request.user.id).count()
    oth_doc = OtherDocument.objects.filter(traveler__user=request.user.id).count()

    return render(request, 'attachment.html', {
        'ref_id': ref_id,
        'fam_att': fam_att,
        'bir_cer': bir_cer,
        'nat_id': nat_id,
        'wed_cer': wed_cer,
        'emb_doc': emb_doc,
        'med_doc': med_doc,
        'oth_doc': oth_doc,

    })


@authentication_required
@allowed_users(allowed_roles=['admin', 'traveler', 'facilitator'])
def my_documents(request):

    ref_id = RefugeeId.objects.filter(traveler__user=request.user)
    fam_att = FamilyAttestation.objects.filter(traveler__user=request.user.id)
    bir_cer = BirthCertificate.objects.filter(traveler__user=request.user.id)
    nat_id = NationalID.objects.filter(traveler__user=request.user.id)
    wed_cer = WeddingCertificate.objects.filter(traveler__user=request.user.id)
    emb_doc = EmbassyDocument.objects.filter(traveler__user=request.user.id)
    med_doc = MedicalDocument.objects.filter(traveler__user=request.user.id)
    oth_doc = OtherDocument.objects.filter(traveler__user=request.user.id)

    return render(request, 'my_documents.html', {
        'ref_id': ref_id,
        'fam_att': fam_att,
        'bir_cer': bir_cer,
        'nat_id': nat_id,
        'wed_cer': wed_cer,
        'emb_doc': emb_doc,
        'med_doc': med_doc,
        'oth_doc': oth_doc,

    })


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator', 'facilitator', 'traveler'])
def add_ref_id(request):
    traveler = get_object_or_404(TravelerRecord, user=request.user)
    attachment = RefugeeId.objects.filter(traveler=traveler)
    if request.method == 'POST':
        traveler = get_object_or_404(TravelerRecord, user=request.user)

        if 'refugee_id' in request.FILES:
            refugee_id_file = request.FILES['refugee_id']
            rec = RefugeeId(traveler=traveler, refugee_id=refugee_id_file)
            rec.save()
            return redirect('attach')
        else:
            return HttpResponse('No file uploaded', status=400)
    return render(request, 'ref_id.html', {'attachment': attachment})


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator', 'facilitator', 'traveler'])
def add_fam_att(request):
    traveler = get_object_or_404(TravelerRecord, user=request.user)
    attachment = FamilyAttestation.objects.filter(traveler=traveler)
    if request.method == 'POST':
        traveler = get_object_or_404(TravelerRecord, user=request.user)

        if 'family_attestation' in request.FILES:
            family_attestation_file = request.FILES['family_attestation']
            rec = FamilyAttestation(traveler=traveler, family_attestation=family_attestation_file)
            rec.save()
            return redirect('attach')
        else:
            return HttpResponse('No file uploaded', status=400)
    return render(request, 'fam_att.html', {'attachment': attachment})


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator', 'facilitator', 'traveler'])
def add_bir_cer(request):
    traveler = get_object_or_404(TravelerRecord, user=request.user)
    attachment = BirthCertificate.objects.filter(traveler=traveler)
    if request.method == 'POST':
        traveler = get_object_or_404(TravelerRecord, user=request.user)

        if 'birth_certificate' in request.FILES:
            birth_certificate_file = request.FILES['birth_certificate']
            rec = BirthCertificate(traveler=traveler, birth_certificate=birth_certificate_file)
            rec.save()
            return redirect('attach')
        else:
            return HttpResponse('No file uploaded', status=400)
    return render(request, 'bir_cer.html', {'attachment': attachment})


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator', 'facilitator', 'traveler'])
def add_nat_id(request):
    traveler = get_object_or_404(TravelerRecord, user=request.user)
    attachment = NationalID.objects.filter(traveler=traveler)
    if request.method == 'POST':
        traveler = get_object_or_404(TravelerRecord, user=request.user)

        if 'national_id' in request.FILES:
            national_id_file = request.FILES['national_id']
            rec = NationalID(traveler=traveler, national_id=national_id_file)
            rec.save()
            return redirect('attach')
        else:
            return HttpResponse('No file uploaded', status=400)
    return render(request, 'nat_id.html', {'attachment': attachment})


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator', 'facilitator', 'traveler'])
def add_wed_cer(request):
    traveler = get_object_or_404(TravelerRecord, user=request.user)
    attachment = WeddingCertificate.objects.filter(traveler=traveler)
    if request.method == 'POST':
        traveler = get_object_or_404(TravelerRecord, user=request.user)

        if 'wedding_certificate' in request.FILES:
            wedding_certificate_file = request.FILES['wedding_certificate']
            rec = WeddingCertificate(traveler=traveler, wedding_certificate=wedding_certificate_file)
            rec.save()
            return redirect('attach')
        else:
            return HttpResponse('No file uploaded', status=400)
    return render(request, 'wed_cer.html', {'attachment': attachment})


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator', 'facilitator', 'traveler'])
def add_emb_doc(request):
    traveler = get_object_or_404(TravelerRecord, user=request.user)
    attachment = EmbassyDocument.objects.filter(traveler=traveler)
    if request.method == 'POST':
        traveler = get_object_or_404(TravelerRecord, user=request.user)

        if 'embassy_document' in request.FILES:
            embassy_document_file = request.FILES['embassy_document']
            rec = EmbassyDocument(traveler=traveler, embassy_document=embassy_document_file)
            rec.save()
            return redirect('attach')
        else:
            return HttpResponse('No file uploaded', status=400)
    return render(request, 'emb_doc.html', {'attachment': attachment})


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator', 'facilitator', 'traveler'])
def add_med_doc(request):
    traveler = get_object_or_404(TravelerRecord, user=request.user)
    attachment = MedicalDocument.objects.filter(traveler=traveler)
    if request.method == 'POST':
        traveler = get_object_or_404(TravelerRecord, user=request.user)

        if 'medical_document' in request.FILES:
            medical_document_file = request.FILES['medical_document']
            rec = MedicalDocument(traveler=traveler, medical_document=medical_document_file)
            rec.save()
            return redirect('attach')
        else:
            return HttpResponse('No file uploaded', status=400)
    return render(request, 'med_doc.html', {'attachment': attachment})


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator', 'facilitator', 'traveler'])
def add_oth_doc(request):
    traveler = get_object_or_404(TravelerRecord, user=request.user)
    attachment = OtherDocument.objects.filter(traveler=traveler)
    if request.method == 'POST':
        traveler = get_object_or_404(TravelerRecord, user=request.user)

        if 'other_document' in request.FILES:
            other_document_file = request.FILES['other_document']
            rec = OtherDocument(traveler=traveler, other_document=other_document_file)
            rec.save()
            return redirect('attach')
        else:
            return HttpResponse('No file uploaded', status=400)
    return render(request, 'oth_doc.html', {'attachment': attachment})


def generic_delete(request, model_name, pk):
    model = apps.get_model('attachments', model_name)
    rec = get_object_or_404(model, id=pk)
    rec.delete()
    messages.success(request, 'Record Deleted')

    referer_url = request.META.get('HTTP_REFERER', 'default_fallback_url')
    return redirect(referer_url)


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator', 'facilitator', 'traveler'])
def del_ref_id(request, pk):
    return generic_delete(request, 'RefugeeId', pk)


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator', 'facilitator', 'traveler'])
def del_fam_att(request, pk):
    return generic_delete(request, 'FamilyAttestation', pk)


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator', 'facilitator', 'traveler'])
def del_bir_cer(request, pk):
    return generic_delete(request, 'BirthCertificate', pk)


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator', 'facilitator', 'traveler'])
def del_nat_id(request, pk):
    return generic_delete(request, 'NationalID', pk)


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator', 'facilitator', 'traveler'])
def del_wed_cer(request, pk):
    return generic_delete(request, 'WeddingCertificate', pk)


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator', 'facilitator', 'traveler'])
def del_emb_doc(request, pk):
    return generic_delete(request, 'EmbassyDocument', pk)


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator', 'facilitator', 'traveler'])
def del_med_doc(request, pk):
    return generic_delete(request, 'MedicalDocument', pk)


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator', 'facilitator', 'traveler'])
def del_oth_doc(request, pk):
    return generic_delete(request, 'OtherDocument', pk)
