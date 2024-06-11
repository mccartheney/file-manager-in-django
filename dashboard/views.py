from django.shortcuts import render, redirect

from .models import folder

from uuid import uuid4


from django.contrib.auth.decorators import login_required

@login_required(login_url="/user/login")
# view to homepage to dashboard
def home_dashboard (request) :

    # render home page
    return render (request, "dashboard/index.html")

@login_required(login_url="/user/login")
def folders_dashboard (request) :
    if request.method == "POST" :
        user = request.user
        user_profile = user.profile
        if request.POST.get("folder_input"):
            folder_name = request.POST.get("folder_input")
            root_folder = user.profile.root_folder
            new_folder = folder.objects.create(
                User = user_profile,
                folder_name = folder_name,
                folder_id = uuid4(),
                parent_folder = root_folder
            )
    folders = request.user.profile.root_folder.children_folder.all()
    folders = reversed(folders)
    # render home page
    return render (request, "dashboard/folders.html", {"folders" : folders})
