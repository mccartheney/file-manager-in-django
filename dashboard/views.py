from django.shortcuts import render, redirect

from .models import folder

from uuid import uuid4

# view to homepage to dashboard
def home_dashboard (request) :
    if request.user.is_authenticated : # if user is logged

        # render home page
        return render (request, "dashboard/index.html")
    else : # if user is not logged
        
        # redirect to login page
        return redirect ("/user/login")

def folders_dashboard (request) :
    if request.user.is_authenticated : # if user is logged
        if request.method == "POST" :
            user = request.user
            user_profile = user.profile
            if request.POST.get("folder_input"):
                folder_name = request.POST.get("folder_input")
                root_folder = user.profile.root_folder
                print(root_folder)
                new_folder = folder.objects.create(
                    User = user_profile,
                    folder_name = folder_name,
                    folder_id = uuid4(),
                    parent_folder = root_folder
                )


        # render home page
        return render (request, "dashboard/folders.html")
    else : # if user is not logged
        
        # redirect to login page
        return redirect ("/user/login")