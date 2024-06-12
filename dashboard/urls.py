from django.urls import path

# import views to show them on dashboard
from .views import home_dashboard, folders_dashboard, folder_dashboard

urlpatterns = [
    path ("", home_dashboard), # path to dashboard homepage
    path ("folders/", folders_dashboard),
    path ("folders/<slug:slug>", folder_dashboard)
]