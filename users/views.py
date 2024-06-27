from django.shortcuts import render, redirect

# import fucntion to login and authenticate user
from django.contrib.auth import login, authenticate

# import User model
from django.contrib.auth.models import User

# import register and login forms
from .forms import change_pass_form, user_profile_form_register, user_profile_form_login

from dashboard.models import folder

from uuid import uuid4

# view to reset Password
def user_view (request) :

    if request.method == "POST" :
        # get user
        user = request.user

        if request.POST.get("new_password") :

            # get new password
            new_password = request.POST.get ("new_password")
            
            # set and save new password
            user.set_password(new_password)
            user.save()

            # loggout user
            return redirect ("/logout")

    return render (request,"users/userPage.html")

# view to make a login
def login_view (request) :
    # if user is authenticated, redirect to main page of the application
    if request.user.is_authenticated :
        return redirect("/dashboard")
        
    if request.method == "POST" : # if method is post
        # get and give post data to form
        request_data = request.POST
        form = user_profile_form_login(request_data)
        
        if form.is_valid() : # if everyting is correct with form
            # get email and pass from form
            user_email_from_form = form.cleaned_data["email"]
            user_pass_from_form = form.cleaned_data["password"]
            
            try : # case exist user with email gived by user
                # get User and username
                user_data = User.objects.get(email = user_email_from_form)
                username = user_data.username

                # authenticate user
                user = authenticate(username=username, password = user_pass_from_form)
                if user : # if email and pass match
                    # login user
                    login (request, user)

                    # on login redirect to main page of application
                    return redirect ("/dashboard")
                else : # if email and pass dont match
                    # warn user
                    warn_message = "⚠️ wrong credentials"
                    return render (request, "users/loginPage/loginPageIndex.html", {"warn_message" : warn_message, "form" : form})

            except : # case dont exist user with email gived by user
                # warn user
                warn_message = "⚠️ Dont exist user with that email"
                return render (request, "users/loginPage/loginPageIndex.html", {"warn_message" : warn_message, "form" : form})
        
        # if form is not valid return login page again
        return render (request, "users/loginPage/loginPageIndex.html", {"form" : form})

    else : # if method is get
        # set formulary
        form = user_profile_form_login()
    
    # return login page with formulary
    return render (request, "users/loginPage/loginPageIndex.html", {"form" : form})

# view to register user
def register_view (request) :

    if request.method == "POST" : # if request method is post
        # get and give post data to form
        request_data = request.POST
        form = user_profile_form_register (request_data)

        if form.is_valid() :# if everyting is correct with form
            # get data from form
            user_name_from_form = form.cleaned_data["name"]
            user_email_from_form = form.cleaned_data["email"]
            user_pass_from_form = form.cleaned_data["password"]

            # get all users and verify if exist any user with email gived by user
            all_users_emails = User.objects.filter().values('email')
            array_of_emails = [user_data["email"] for user_data in all_users_emails]

            
            if user_email_from_form in array_of_emails : # if exist any user with email gived by them
                # warn user
                warn_message = "⚠️ Already exist a user with that email !"
                return render (request, "users/registerPage.html", {"warn_message" : warn_message, "form" : form})
            else : # if dont exist any user with email gived by them
                # create new user with data gived by user
                new_user = User.objects.create_user(
                    username=f'{user_name_from_form} -{user_email_from_form}-', 
                    email=user_email_from_form, 
                    password=user_pass_from_form
                )
                new_user.save()

                # create new user_profile with User created above and data gived by user
                new_user_profile = form.save(commit=False)
                new_user_profile.user = new_user
                new_user_profile.name = user_name_from_form
                new_user_profile.email = user_email_from_form
                new_user_profile.password = user_pass_from_form
                new_user_profile.max_storage = 50
                new_user_profile.save()

                new_master_folder = folder.objects.create(
                    User = new_user_profile,
                    folder_id = str(uuid4()),
                    folder_name = "root",
                    folder_visible_name = "root" 
                )
                new_master_folder.save()

                # if user is created redirect to login page
                return redirect("/user/login")

        # if form is not valid return login page again
        return render (request, "users/registerPage/registerPageIndex.html", {"form" : form})

    else : # if method is get
        # return login page with formulary
        form = user_profile_form_register()

    # return register page with form
    return render (request, "users/registerPage/registerPageIndex.html", {"form" : form})