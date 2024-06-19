from django.urls import path

# import views to show them on dashboard
from .views import home_dashboard, folders_dashboard, folder_dashboard

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path ("", home_dashboard), # path to dashboard homepage
    path ("folders/", folders_dashboard),
    path ("folders/<slug:slug>", folder_dashboard)
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)