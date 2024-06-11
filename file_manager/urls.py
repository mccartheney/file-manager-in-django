from django.contrib import admin
from django.urls import path, include

# import views form file_manager app
from .views import home_page, logoutPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home_page), # home path
    path("logout/",logoutPage),
    path("user/", include("users.urls")), # users (login and register) pages
    path("dashboard/", include ("dashboard.urls")) # dashboard (file manager) pages
]
