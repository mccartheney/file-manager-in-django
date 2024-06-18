# render and redirect to render a page or redirect user to other page
from django.shortcuts import render, redirect

# import folder model to manage folders
from .models import folder

# import uuid to create unique random ids
from uuid import uuid4

# import login required to make pages login required
from django.contrib.auth.decorators import login_required

from .forms import file_form

# view to homepage to dashboard
@login_required(login_url="/user/login")
def home_dashboard (request) :

    # render home page
    return render (request, "dashboard/index.html")

# view to file manager (on root folder)
@login_required(login_url="/user/login")
def folders_dashboard (request) :
    # create a empty warn message to hove global acess inside this scope
    warn_message = ""

    # get root folder (main folder, where all is inside and cannot be deleted), and her name
    root_folder = request.user.profile.folders.all().filter(parent_folder = None).filter(folder_name="root")[0]
    root_folder_name = root_folder.folder_name

    if request.method == "POST" : # if user send something

        # get user and user profile to link the file or the folder to them  
        user = request.user
        user_profile = user.profile

        if request.POST.get("folder_to_rename") : # if the user send a new name to a folder

            # get the necessary data to modify folder:

            # folder id
            folder_id_to_rename = request.POST.get ("folder_id_to_rename")
            # get folder by id
            folder_to_rename = user_profile.folders.all().filter(folder_id = folder_id_to_rename)[0]
            # rename thet folder
            folder_to_rename.folder_name = request.POST.get("folder_to_rename")

            # save the changes
            folder_to_rename.save()

            # get all folders inside root folder
            folders = root_folder.children_folder.all()
            folders = reversed(folders)

            # return html page with necessary data
            return render (request, "dashboard/folders.html", {"folders":folders, "folder_name" : root_folder_name})

        if request.POST.get("folder_to_remove"): # if user send a folder to remove
            
            # get the necessary data to remove that folder:

            # get id of the folder to delete
            folder_id_to_delete = request.POST.get("folder_to_remove")
            # get folder to delete by id
            folder_to_delete = user_profile.folders.all().filter(folder_id = folder_id_to_delete)

            # delte that folder
            folder_to_delete.delete()

            # get all folders inside root folder
            folders = root_folder.children_folder.all()
            folders = reversed(folders)

            # return html page with necessary data
            return render (request, "dashboard/folders.html", {"folders":folders, "folder_name" : root_folder_name})

        if request.POST.get("folder_input"): # if user send a folder to create

            # get the name of the new folder
            folder_name = request.POST.get("folder_input")
            # get how many folder with the same name exists
            exists_folder_with_same_name = root_folder.children_folder.all().filter(folder_name = folder_name)
                
            # get all folders inside root folder
            folders = root_folder.children_folder.all()
            folders = reversed(folders)

            if exists_folder_with_same_name : # if exist any folder with the same name, warn it to user
                warn_message = "You already have folders with that name, try other name"

                # return html page with necessary data
                return render (request, "dashboard/folders.html", {"folders":folders, "folder_name" : root_folder_name, "warn_message":warn_message})

            # create the new folder
            new_folder = folder.objects.create(
                User = user_profile,
                folder_name = folder_name,
                folder_id = uuid4(),
                parent_folder = root_folder
            )


    # get all folders inside root folder
    folders = root_folder.children_folder.all()
    if folders : # if have folders, invert them
        folders = reversed(folders)

    upload_file_form = file_form()

    # return html page with necessary data
    return render (request, "dashboard/folders.html", {"folders" : folders, "folder_name" : root_folder_name, "file_form" : upload_file_form})

# view to file manager (not on root folder)
@login_required(login_url="/user/login")
def folder_dashboard (request, slug) :  
    # create a empty warn message to hove global acess inside this scope
    warn_message = ""

    # get folder id by slug (paremeter from url)
    folder_id = slug

    # get user profile (folders are connected to them) 
    user_profile = request.user.profile

    # get actual folder and folder name by id
    this_folder = request.user.profile.folders.all().filter(folder_id = folder_id)[0]
    this_folder_name = this_folder.folder_name

    # get all folder inside the folder the user are in
    folders = this_folder.children_folder.all()
    
    # get a parent id to go to them on press return button
    parent_id = this_folder.parent_folder.folder_id
    print(parent_id)

    if this_folder.parent_folder.parent_folder == None :
        parent_id = ""

    if (request.method == "POST") : # if user sent something 
        if request.POST.get("folder_to_rename") : # if user send a folder to rename
            
            # get the necessary data to rename that folder:

            # get folder id
            folder_id_to_rename = request.POST.get ("folder_id_to_rename")
            # get folder to renam by id
            folder_to_rename = folders.filter(folder_id = folder_id_to_rename)[0]

            # rename the folder
            folder_to_rename.folder_name = request.POST.get("folder_to_rename")

            # save the changes
            folder_to_rename.save()

            # get folder inside the actual folder
            folders = this_folder.children_folder.all()
            folders = reversed(folders)

            # return html page with necessary data
            return render (request, "dashboard/folders.html", {"folders":folders, "folder_name" : this_folder.folder_name})


        if request.POST.get("folder_to_remove"): # if user send a folder to remove

            # get the necessary data to remove that folder:
            
            # get id folder
            folder_id_to_delete = request.POST.get("folder_to_remove")
            # get folder by id
            folder_to_delete = folders.filter(folder_id = folder_id_to_delete)

            # delete that folder
            folder_to_delete.delete()

            # get folders inside that folders
            folders = this_folder.children_folder.all()
            folders = reversed(folders)

            # return html page with necessary data
            return render (request, "dashboard/folders.html", {"folders":folders, "folder_name" : this_folder_name})

        # get folder name to create
        folder_name = request.POST.get("folder_input")

        # set parent folder the actual folder
        parent_folder = this_folder

        # get all folders inside the actual folder to see if have the same name as the new one
        exists_folder_with_same_name = this_folder.children_folder.all().filter(folder_name = folder_name)

        if exists_folder_with_same_name : # if dome one have the same name, warn it to user
            warn_message = "You already have folders with that name, try other name"

            # return html page with necessary data
            return render (request, "dashboard/folders.html", {"folders":folders,"folder_id" : this_folder.folder_id, "folder_name" : this_folder_name, "parent_id":parent_id, "warn_message":warn_message})

        # create folder
        new_folder = folder.objects.create(
            User = user_profile,
            folder_name = folder_name,
            folder_id = uuid4(),
            parent_folder = parent_folder
        )
    
    # return html page with necessary data
    return render (request, "dashboard/folder.html", {"folders":folders,"folder_id" : this_folder.folder_id, "folder_name" : this_folder_name, "parent_id":parent_id, "warn_message":warn_message})
