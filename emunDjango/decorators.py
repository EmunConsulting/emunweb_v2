from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger
from functools import wraps
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

from constants import RECORDS_PER_PAGE_DEFAULT


# Authentication Check
def authentication_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            messages.error(request, "Access denied")
            return redirect('login')

    return wrapper


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('login')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.groups.exists():
                user_groups = [group.name for group in request.user.groups.all()]
                if any(group in allowed_roles for group in user_groups):
                    return view_func(request, *args, **kwargs)
            print('working: ', allowed_roles)
            return redirect('access_denied')
        return wrapper_func
    return decorator


def paginate(template_name=None, default_records_per_page=10):
    def decorator(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            # Define the default records per page
            RECORDS_PER_PAGE_DEFAULT = default_records_per_page

            response = func(request, *args, **kwargs)

            if isinstance(response, dict):
                # If the view returns a dictionary (context), handle pagination
                data = response.get('data')
                paginator = response.get('paginator')

                # Get the current page number
                page_number = request.GET.get('page', 1)

                # Get the records per page
                records_per_page = request.GET.get('recordsPerPage', RECORDS_PER_PAGE_DEFAULT)
                try:
                    records_per_page = int(records_per_page)
                except ValueError:
                    records_per_page = RECORDS_PER_PAGE_DEFAULT

                # Paginate the data
                try:
                    paginated_data = paginator.page(page_number)
                except PageNotAnInteger:
                    paginated_data = paginator.page(1)
                except EmptyPage:
                    paginated_data = paginator.page(paginator.num_pages)

                response['data'] = paginated_data
                response['recordsPerPage'] = records_per_page

            if isinstance(response, dict) and template_name:
                return render(request, template_name, response)
            else:
                return response

        return wrapper

    return decorator


def delete_and_redirect(redirect_url, model):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, pk):
            model_instance = get_object_or_404(model, id=pk)
            model_instance.delete()
            messages.success(request, "Record Deleted")
            return redirect(redirect_url)

        return wrapper

    return decorator

