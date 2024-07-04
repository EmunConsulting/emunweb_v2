from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_user, name='register'),
    path('add_traveler_record/', views.add_traveler_record, name='add_traveler_record'),
    path('upload_profile_image', views.upload_profile_image, name='upload_profile_image'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('access_denied', views.access_denied, name='access_denied'),
    path('date_converter', views.date_converter, name='date_converter'),
    path('gregorian_to_ethiopian', views.date_converter, name='gregorian_to_ethiopian'),
    path('convert/', views.convert, name='convert'),
]
