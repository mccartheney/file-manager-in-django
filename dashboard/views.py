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

    warn_message = ""

    root_folder = request.user.profile.folders.all().filter(parent_folder = None).filter(folder_name="root")[0]
    root_folder_name = root_folder.folder_name

    folders = root_folder.children_folder.all()
    folders = reversed(folders)

    if request.method == "POST" :
        user = request.user
        user_profile = user.profile

        if request.POST.get("folder_to_rename") :
            folder_id_to_rename = request.POST.get ("folder_id_to_rename")
            folder_to_rename = user_profile.folders.all().filter(folder_id = folder_id_to_rename)[0]
            folder_to_rename.folder_name = request.POST.get("folder_to_rename")

            folder_to_rename.save()

            folders = root_folder.children_folder.all()
            folders = reversed(folders)

            return render (request, "dashboard/folders.html", {"folders":folders, "folder_name" : root_folder_name})

        if request.POST.get("folder_to_remove"):
            folder_id_to_delete = request.POST.get("folder_to_remove")
            folder_to_delete = user_profile.folders.all().filter(folder_id = folder_id_to_delete)

            folder_to_delete.delete()

            folders = root_folder.children_folder.all()
            folders = reversed(folders)

            return render (request, "dashboard/folders.html", {"folders":folders, "folder_name" : root_folder_name})

        if request.POST.get("folder_input"):
            folder_name = request.POST.get("folder_input")
            exists_folder_with_same_name = root_folder.children_folder.all().filter(folder_name = folder_name)
                
            if exists_folder_with_same_name :
                warn_message = "You already have folders with that name, try other name"
                print(folders)
                return render (request, "dashboard/folders.html", {"folders":folders, "folder_name" : root_folder_name, "warn_message":warn_message})


            new_folder = folder.objects.create(
                User = user_profile,
                folder_name = folder_name,
                folder_id = uuid4(),
                parent_folder = root_folder
            )

    folders = root_folder.children_folder.all()
    if folders :
        folders = reversed(folders)


    # render home page
    return render (request, "dashboard/folders.html", {"folders" : folders, "folder_name" : root_folder_name})


@login_required(login_url="/user/login")
def folder_dashboard (request, slug) :  
    folder_id = slug
    user_profile = request.user.profile
    this_folder = request.user.profile.folders.all().filter(folder_id = folder_id)[0]
    this_folder_name = this_folder.folder_name
    folders = this_folder.children_folder.all()
    warn_message = ""
    parent_id = this_folder.parent_folder

    if parent_id.parent_folder == None :
        parent_id = ""
    else :
        parent_id = parent_id.folder_id


    if (request.method == "POST") :
        folder_name = request.POST.get("folder_input")
        parent_folder = this_folder
        exists_folder_with_same_name = this_folder.children_folder.all().filter(folder_name = folder_name)
        print("on post")
        print(request.POST)
        if request.POST.get("folder_to_rename") :
            print("on rename")
            folder_id_to_rename = request.POST.get ("folder_id_to_rename")
            folder_to_rename = folders.filter(folder_id = folder_id_to_rename)[0]
            folder_to_rename.folder_name = request.POST.get("folder_to_rename")

            folder_to_rename.save()

            folders = this_folder.children_folder.all()
            folders = reversed(folders)

            print(this_folder.folder_name)

            return render (request, "dashboard/folders.html", {"folders":folders, "folder_name" : this_folder.folder_name})


        if request.POST.get("folder_to_remove"):
            print("on remove")
            folder_id_to_delete = request.POST.get("folder_to_remove")
            folder_to_delete = folders.filter(folder_id = folder_id_to_delete)
            folder_to_delete.delete()
            folders = this_folder.children_folder.all()
            folders = reversed(folders)

            return render (request, "dashboard/folder.html", {"folders":folders, "folder_name" : this_folder_name})


        if exists_folder_with_same_name :
            warn_message = "You already have folders with that name, try other name"
            return render (request, "dashboard/folder.html", {"folders":folders,"folder_id" : this_folder.folder_id, "folder_name" : this_folder_name, "parent_id":parent_id, "warn_message":warn_message})


        new_folder = folder.objects.create(
            User = user_profile,
            folder_name = folder_name,
            folder_id = uuid4(),
            parent_folder = parent_folder
        )
    
    

    print(parent_id)

    return render (request, "dashboard/folder.html", {"folders":folders,"folder_id" : this_folder.folder_id, "folder_name" : this_folder_name, "parent_id":parent_id, "warn_message":warn_message})
