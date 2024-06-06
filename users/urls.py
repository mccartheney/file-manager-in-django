from django.urls import path

# import views to create urls
from .views import login_view, register_view

urlpatterns = [
    path ('login/', login_view), # login path
    path ('register/', register_view) # register path
]