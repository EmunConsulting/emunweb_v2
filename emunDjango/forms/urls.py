from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('form', views.form, name='form'),
    path('submit_form', views.submit_form, name='submit_form'),

]
