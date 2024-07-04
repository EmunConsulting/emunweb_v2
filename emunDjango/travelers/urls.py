from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('profile_info', views.profile_info, name='profile_info'),
    path('list_my_applications', views.list_my_applications, name='list_my_applications'),
    path('compiled_application/<int:pk>', views.compiled_application, name='compiled_application'),
]
