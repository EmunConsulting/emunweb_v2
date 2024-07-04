from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('visa_application/', views.visa_application, name='visa_application'),
    path('applicant_personal_data/<str:application_number>/', views.applicant_personal_data, name='applicant_personal_data'),
    path('applicant_travel_document/<str:application_number>/', views.applicant_travel_document, name='applicant_travel_document'),
    path('applicant_home_address/<str:application_number>/', views.applicant_home_address, name='applicant_home_address'),
    path('travel_information/<str:application_number>/', views.travel_information, name='travel_information'),
    path('reference/<str:application_number>/', views.reference, name='reference'),
    path('end_of_form/', views.end_of_form, name='end_of_form'),

    # Update
    path('update_applicant_home_address/<str:application_number>/', views.update_applicant_home_address, name='update_applicant_home_address'),
    path('update_applicant_personal_data/<str:application_number>/', views.update_applicant_personal_data, name='update_applicant_personal_data'),
    path('update_applicant_travel_document/<str:application_number>/', views.update_applicant_travel_document, name='update_applicant_travel_document'),
    path('update_travel_information/<str:application_number>/', views.update_travel_information, name='update_travel_information'),
    path('update_reference/<str:application_number>/', views.update_reference, name='update_reference'),
]