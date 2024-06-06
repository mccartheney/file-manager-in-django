from django.urls import path

# import views to show them on dashboard
from .views import home_dashboard

urlpatterns = [
    path ("", home_dashboard) # path to dashboard homepage
]