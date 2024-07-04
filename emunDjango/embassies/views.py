from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from decorators import paginate, authentication_required, allowed_users
from utils import get_records_per_page
from .models import Embassy

# Create your views here.

@authentication_required
@allowed_users(allowed_roles=['admin', 'traveler'])
@paginate(template_name='embassies.html')
def embassy(request):

    embassies = Embassy.objects.all()

    records_per_page = get_records_per_page(request)
    paginator = Paginator(embassies, records_per_page)

    return {'data': paginator.page(1),
            'paginator': paginator,
            }