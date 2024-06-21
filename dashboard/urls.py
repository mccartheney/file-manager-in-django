from django.urls import path

# import views to show them on dashboard
from .views import home_dashboard, folders, files,file_manager_dashboard, file_manager_folder_dashboard




urlpatterns = [
    path ("", home_dashboard), # path to dashboard homepage
    path ("filemanager/", file_manager_dashboard),
    path ("filemanager/<slug:slug>", file_manager_folder_dashboard),
    path("folders/", folders),
    path("files/", files),
]

