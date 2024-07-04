from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('facilitators.urls')),
    path('', include('embassies.urls')),
    path('', include('forms.urls')),
    path('', include('travelers.urls')),
    path('', include('attachments.urls')),
    path('', include('payments.urls')),
    path('', include('tasks.urls')),
    path('', include('notifications.urls')),
    path('', include('visaapplications.urls')),
    path('', include('reports.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
