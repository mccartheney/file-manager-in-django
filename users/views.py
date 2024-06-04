from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from .forms import user_profile_form_register

def login_view (request) :
    return render (request, "users/loginPage.html")

def register_view (request) :

    if request.method == "POST" :
        request_data = request.POST
        form = user_profile_form_register (request_data)

        if form.is_valid() :
            
            user_name_from_form = form.cleaned_data["name"]
            user_email_from_form = form.cleaned_data["email"]
            user_pass_from_form = form.cleaned_data["password"]

            all_users_emails = User.objects.filter().values('email')
            array_of_emails = [user_data["email"] for user_data in all_users_emails]

            print(array_of_emails)

            if user_email_from_form in array_of_emails :
                warn_menssage = "⚠️ Already exist a user with that email !"
                return render (request, "users/registerPage.html", {"warn_menssage" : warn_menssage, "form" : form})
            else :
                new_user = User.objects.create_user(username=f'{user_name_from_form} <{user_email_from_form}>', email=user_email_from_form, password=user_pass_from_form)
                new_user.save()

                new_user_profile = form.save(commit=False)
                new_user_profile.user = new_user
                new_user_profile.name = user_name_from_form
                new_user_profile.email = user_email_from_form
                new_user_profile.password = user_pass_from_form

                new_user_profile.save()

        return render (request, "users/registerPage.html")


    else :
        form = user_profile_form_register()

    return render (request, "users/registerPage.html", {"form" : form})