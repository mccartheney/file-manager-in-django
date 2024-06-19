from django.urls import path

# import views to create urls
from .views import login_view, register_view, user_view

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', user_view),
    path ('login/', login_view), # login path
    path ('register/', register_view), # register path

    # reset pass paths
    path ('reset_password/', auth_views.PasswordResetView.as_view(template_name="users/resetPassPages/resetPassPage.html"), name="reset_password"),
    path ("reset_password_sent/", auth_views.PasswordResetDoneView.as_view(template_name="users/resetPassPages/resetPassSent.html"), name="password_reset_done"),
    path ("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="users/resetPassPages/resetPassChange.html"), name="password_reset_confirm"),
    path ("reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(template_name="users/resetPassPages/resetPassComplete.html"), name="password_reset_complete"),
]