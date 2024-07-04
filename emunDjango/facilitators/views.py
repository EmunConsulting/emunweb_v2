from django.contrib.auth.models import User, Group

from decorators import paginate, authentication_required, allowed_users
from utils import get_records_per_page

from datetime import date, datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib import messages

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count

from .models import Role, Account
from travelers.models import TravelerRecord
from visaapplications.models import VisaApplication


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator'])
@paginate(template_name='tasks_and_assignments.html')
def tasks_and_assignments(request):

    visa_app = VisaApplication.objects.all()

    records_per_page = get_records_per_page(request)
    paginator = Paginator(visa_app, records_per_page)

    return {'data': paginator.page(1),
            'paginator': paginator,
            }


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator'])
def assign_task(request, application_number):

    # Get the groups
    facilitator_group = Group.objects.get(name='facilitator')
    moderator_group = Group.objects.get(name='moderator')

    visa_app = VisaApplication.objects.get(application_number=application_number)
    # Filter users based on group membership
    person = User.objects.filter(groups__in=[facilitator_group, moderator_group]).distinct()

    if request.method == "POST":
        visa_app.application_status = 2

        assigned_to_id = request.POST['assigned_officer']
        assigned_to = get_object_or_404(User, id=assigned_to_id)

        visa_app.assigned_officer = assigned_to
        visa_app.save()
        messages.success(request, "Task Assigned")
        return redirect('tasks_and_assignments')

    else:
        return render(request, 'assign_task.html', {
            'visa_app': visa_app,
            'person': person,
        })


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator', 'facilitator'])
def assigned_to_me(request):

    user_id = request.user.id

    visa_app = VisaApplication.objects.filter(assigned_officer=user_id)

    return render(request, 'tasks_assigned_to_me.html', {
        'visa_app': visa_app,
    })


@authentication_required
@allowed_users(allowed_roles=['admin', 'moderator', 'facilitator'])
def add_officer_note(request, application_number):

    visa_app = VisaApplication.objects.get(application_number=application_number)

    if request.method == "POST":
        visa_app.application_status = 3
        visa_app.officer_notes = request.POST['officer_notes']

        visa_app.save()
        messages.success(request, "Note Added")
        return redirect('assigned_to_me')

    else:
        return render(request, 'add_officer_note.html', {
            'visa_app': visa_app,
        })

# ====================================================================OLD WORK BUT STILL FUNCTIONAL =
# ====================================================================CREATE =======================

@authentication_required
@allowed_users(allowed_roles=['admin', ])
def add_role(request):
    roles = Role.objects.all()

    if request.method == "POST":
        role = request.POST['role']

        new_rec = Role(
            role=role,
        )
        new_rec.save()
        messages.success(request, "Record Added")

        if 'save_stay' in request.POST:
            return redirect('add_role')
        elif 'save_redirect' in request.POST:
            return redirect('role')

    else:
        return render(request, 'add_role.html', {
            'roles': roles,
        })


# ====================================================================READ =======================

@authentication_required
@allowed_users(allowed_roles=['admin'])
@paginate(template_name='roles.html')
def role(request):

    roles = Role.objects.all()

    records_per_page = get_records_per_page(request)
    paginator = Paginator(roles, records_per_page)

    return {'data': paginator.page(1),
            'paginator': paginator,
            }


@authentication_required
@allowed_users(allowed_roles=['admin'])
@paginate(template_name='accounts.html')
def account(request):

    accounts = Account.objects.all()

    records_per_page = get_records_per_page(request)
    paginator = Paginator(accounts, records_per_page)

    return {'data': paginator.page(1),
            'paginator': paginator,
            }


# ====================================================================UPDATE =======================

@authentication_required
@allowed_users(allowed_roles=['admin'])
def update_role(request, pk):
    rec = Role.objects.get(id=pk)

    if request.method == "POST":
        rec.role = request.POST['role']
        rec.save()

        messages.success(request, "Record Updated")
        return redirect('role')

    else:
        return render(request, 'update_role.html', {
            'rec': rec,
        })


# ====================================================================DELETE =======================
@authentication_required
@allowed_users(allowed_roles=['admin'])
def delete_role(request, pk):
    rec = get_object_or_404(Role, id=pk)
    # Check if there are references in PlannedFeeResponse
    if Account.objects.filter(role=rec).exists():
        messages.error(request, "This role is used in a record. It can't be deleted")
    else:
        rec.delete()
        messages.success(request, "Record Deleted")

    return redirect('role')
