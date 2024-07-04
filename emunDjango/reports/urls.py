from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('general_report', views.general_report, name='general_report'),
    path('account_list', views.account_list, name='account_list'),
    path('visa_application_list', views.visa_application_list, name='visa_application_list'),

]
