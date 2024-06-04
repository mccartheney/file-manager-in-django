from django.contrib import admin
from django.urls import path, include

# import views form file_manager app
from .views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home_page), # home path
    path("user/", include("users.urls")) # users (login and register) pages
]
