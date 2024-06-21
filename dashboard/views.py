# render and redirect to render a page or redirect user to other page
from django.shortcuts import render, redirect

# import folder model to manage folders
from .models import folder

# import uuid to create unique random ids
from uuid import uuid4

# import login required to make pages login required
from django.contrib.auth.decorators import login_required

from .forms import file_form

from .models import file

from .functionalities import get_type_files_size

# view to homepage to dashboard
@login_required(login_url="/user/login")
def home_dashboard (request) :
    all_files = request.user.profile.files.all()
    file_sizes = get_type_files_size(all_files=all_files)
    file_types = file_sizes.keys()
    used_storage = sum(file_sizes.values())
    total_storage = 50
    used_porcentage =  round((used_storage/total_storage) * 100)
    used_float_porcentage = (used_storage/total_storage) * 100
    left_porcentage = round(100 - used_float_porcentage,2)

    print (file_sizes)

    # render home page
    return render (request, "dashboard/index.html", {"file_sizes":file_sizes, "used_storage" :used_storage, "total_storage" : total_storage, "file_types":file_types, "used_porcentage":used_porcentage, "used_float_porcentage" : used_float_porcentage, "left_porcentage":left_porcentage})

# view to file manager (on root folder)
@login_required(login_url="/user/login")
def file_manager_dashboard (request) :
    # create a empty warn message to hove global acess inside this scope
    warn_message = ""

    # get root folder (main folder, where all is inside and cannot be deleted), and her name
    root_folder = request.user.profile.folders.all().filter(parent_folder = None).filter(folder_name="root")[0]
    root_folder_name = root_folder.folder_name

    children_files = root_folder.children_files.all()


    if request.method == "POST" : # if user send something

        # get user and user profile to link the file or the folder to them  
        user = request.user
        user_profile = user.profile

        if request.POST.get("file_to_remove") :

            id_file_to_delete = request.POST.get("file_to_remove")
            folder_to_delete = children_files.filter(file_id = id_file_to_delete)[0]

            folder_to_delete.delete()

            # get all folders inside root folder
            folders = root_folder.children_folder.all()
            folders = reversed(folders)

            children_files = root_folder.children_files.all()

            upload_file_form = file_form()

            # return html page with necessary data
            return render (request, "dashboard/fileManagerRoot.html", {"folders" : folders, "folder_name" : root_folder_name, "file_form" : upload_file_form, "files": children_files})

        if request.POST.get("folder_to_rename") : # if the user send a new name to a folder


            # get the necessary data to modify folder:

            # folder id
            folder_id_to_rename = request.POST.get ("folder_id_to_rename")
            # get folder by id
            folder_to_rename = user_profile.folders.all().filter(folder_id = folder_id_to_rename)[0]


            folder_with_the_same_name = root_folder.children_folder.all().filter(folder_name = request.POST.get("folder_to_rename"))

            if folder_with_the_same_name:

                # get all folders inside root folder
                folders = root_folder.children_folder.all()
                folders = reversed(folders)

                children_files = root_folder.children_files.all()

                upload_file_form = file_form()

                warn_message = "You already have folders with that name, try other name"

                # return html page with necessary data
                return render (request, "dashboard/fileManagerRoot.html", {"folders":folders, "folder_name" : root_folder_name, "warn_message":warn_message, "file_form" : upload_file_form, "files": children_files})

            # rename thet folder
            folder_to_rename.folder_visible_name = request.POST.get("folder_to_rename")
            folder_to_rename.folder_name = request.POST.get("folder_to_rename")

            # save the changes
            folder_to_rename.save()

            # get all folders inside root folder
            folders = root_folder.children_folder.all()
            folders = reversed(folders)

            children_files = root_folder.children_files.all()

            upload_file_form = file_form()

            # return html page with necessary data
            return render (request, "dashboard/fileManagerRoot.html", {"folders" : folders, "folder_name" : root_folder_name, "file_form" : upload_file_form, "files": children_files})

        elif request.POST.get("folder_to_remove"): # if user send a folder to remove
            
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


            upload_file_form = file_form()

            # return html page with necessary data
            return render (request, "dashboard/fileManagerRoot.html", {"folders" : folders, "folder_name" : root_folder_name, "file_form" : upload_file_form, "files": children_files})

        elif request.POST.get("folder_input"): # if user send a folder to create

            # get the name of the new folder
            folder_name = request.POST.get("folder_input")
            folder_visible_name = request.POST.get("folder_input")
            # get how many folder with the same name exists
            exists_folder_with_same_name = root_folder.children_folder.all().filter(folder_name = folder_name)
            children_files = root_folder.children_files.all()

            upload_file_form = file_form()

            # get all folders inside root folder
            folders = root_folder.children_folder.all()
            folders = reversed(folders)

            if exists_folder_with_same_name : # if exist any folder with the same name, warn it to user
                folder_visible_name = f'{folder_name} ({len(exists_folder_with_same_name)})'

               

            # create the new folder
            new_folder = folder.objects.create(
                User = user_profile,
                folder_name = folder_name,
                folder_id = uuid4(),
                parent_folder = root_folder,
                folder_visible_name = folder_visible_name
            )

            children_files = root_folder.children_files.all()

            upload_file_form = file_form()

            # get all folders inside root folder
            folders = root_folder.children_folder.all()
            folders = reversed(folders)

            # return html page with necessary data
            return render (request, "dashboard/fileManagerRoot.html", {"folders":folders, "folder_name" : root_folder_name, "file_form" : upload_file_form, "files": children_files})
        
        else :
            file_from_user =request.FILES["files"]
            file_name_from_user = str(request.FILES["files"])
            visible_file_name_from_user = str(request.FILES["files"])

            file_with_same_name = children_files.filter(file_name = file_name_from_user)

            if file_with_same_name :
                visible_file_name_from_user = f"{file_name_from_user} ({len(file_with_same_name)})"

            new_file = file.objects.create(
                User = user_profile,
                file = file_from_user,
                file_id = uuid4(),
                file_visible_name = visible_file_name_from_user,
                file_name = file_name_from_user,
                parent_folder = root_folder
            )
       


    # get all folders inside root folder
    folders = root_folder.children_folder.all()
    if folders : # if have folders, invert them
        folders = reversed(folders)

    upload_file_form = file_form()

    # return html page with necessary data
    return render (request, "dashboard/fileManagerRoot.html", {"folders" : folders, "folder_name" : root_folder_name, "file_form" : upload_file_form, "files": children_files})

# view to file manager (not on root folder)
@login_required(login_url="/user/login")
def file_manager_folder_dashboard (request, slug) :
    

    # create a empty warn message to hove global acess inside this scope
    warn_message = ""

    # get folder id by slug (paremeter from url)
    folder_id = slug

    # get user profile (folders are connected to them) 
    user_profile = request.user.profile

    # get actual folder and folder name by id
    this_folder = request.user.profile.folders.all().filter(folder_id = folder_id)[0]

    this_folder_name = this_folder.folder_name


    path_to_root = []
    path_quantity = 0
    root_folder = request.user.profile.folders.all().filter(parent_folder = None, folder_name="root").first()
    actual_folder_search = this_folder
    actual_parent_folder = this_folder.parent_folder

    while True :
        path_quantity += 1
        path_to_root
        path_to_root.append(actual_folder_search)
        
        if actual_folder_search == root_folder :
            path_to_root = reversed(path_to_root)
            break

        actual_folder_search = actual_parent_folder
        actual_parent_folder = actual_folder_search.parent_folder
    children_files = this_folder.children_files.all()

    # get all folder inside the folder the user are in
    folders = this_folder.children_folder.all()

    upload_file_form = file_form()

    # get a parent id to go to them on press return button
    parent_id = this_folder.parent_folder.folder_id
    print(parent_id)

    if this_folder.parent_folder.parent_folder == None :
        parent_id = ""

    if (request.method == "POST") : # if user sent something 
        print(request.FILES)
        if request.POST.get("file_to_remove") :

            id_file_to_delete = request.POST.get("file_to_remove")
            file_to_delete = children_files.filter(file_id = id_file_to_delete)[0]

            file_to_delete.delete()

            # get actual folder and folder name by id
            this_folder = request.user.profile.folders.all().filter(folder_id = folder_id)[0]
            this_folder_name = this_folder.folder_name

            children_files = this_folder.children_files.all()

            upload_file_form = file_form()

            # return html page with necessary data

            return render (request, "dashboard/fileManagerFolder.html", {"folders":folders,"folder_id" : this_folder.folder_id, "folder_name" : this_folder_name, "parent_id":parent_id, "file_form" : upload_file_form, "files": children_files})



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

           # get actual folder and folder name by id
            this_folder = request.user.profile.folders.all().filter(folder_id = folder_id)[0]
            this_folder_name = this_folder.folder_name

            children_files = this_folder.children_files.all()

            upload_file_form = file_form()

            # return html page with necessary data

            return render (request, "dashboard/fileManagerFolder.html", {"folders":folders,"folder_id" : this_folder.folder_id, "folder_name" : this_folder_name, "parent_id":parent_id, "file_form" : upload_file_form, "files": children_files})


        if request.POST.get("folder_to_remove"): # if user send a folder to remove

            # get the necessary data to remove that folder:
            
            # get id folder
            folder_id_to_delete = request.POST.get("folder_to_remove")
            # get folder by id
            folder_to_delete = folders.filter(folder_id = folder_id_to_delete)

            # delete that folder
            folder_to_delete.delete()

            # get actual folder and folder name by id
            this_folder = request.user.profile.folders.all().filter(folder_id = folder_id)[0]
            this_folder_name = this_folder.folder_name

            children_files = this_folder.children_files.all()

            upload_file_form = file_form()

            # return html page with necessary data

            return render (request, "dashboard/fileManagerFolder.html", {"folders":folders,"folder_id" : this_folder.folder_id, "folder_name" : this_folder_name, "parent_id":parent_id, "file_form" : upload_file_form, "files": children_files})

        
        elif request.POST.get("folder_input") :# get folder name to create
            folder_name = request.POST.get("folder_input")
            folder_visible_name = request.POST.get("folder_input")
            # set parent folder the actual folder
            parent_folder = this_folder

            # get all folders inside the actual folder to see if have the same name as the new one
            exists_folder_with_same_name = this_folder.children_folder.all().filter(folder_name = folder_name)

            if exists_folder_with_same_name : # if dome one have the same name, warn it to user

                folder_visible_name = f'{folder_name} ({len(exists_folder_with_same_name)})'
                

            # create folder
            new_folder = folder.objects.create(
                User = user_profile,
                folder_name = folder_name,
                folder_id = uuid4(),
                parent_folder = this_folder,
                folder_visible_name = folder_visible_name
            )
        else :
            file_from_user =request.FILES["files"]
            file_name_from_user = str(request.FILES["files"])
            visible_file_name_from_user = str(request.FILES["files"])

            file_with_same_name = children_files.filter(file_name = file_name_from_user)

            if file_with_same_name :
                visible_file_name_from_user = f"{file_name_from_user} ({len(file_with_same_name)})"

            new_file = file.objects.create(
                User = user_profile,
                file = file_from_user,
                file_id = uuid4(),
                file_visible_name = visible_file_name_from_user,
                file_name = file_name_from_user,
                parent_folder = this_folder
            )



    this_folder = request.user.profile.folders.all().filter(folder_id = folder_id)[0]
    this_folder_name = this_folder.folder_visible_name

    children_files = this_folder.children_files.all()

    upload_file_form = file_form()

    print(path_quantity-1)

    # return html page with necessary data
    return render (request, "dashboard/fileManagerFolder.html", {"folders":folders,"folder_id" : this_folder.folder_id, "folder_name" : this_folder_name, "parent_id":parent_id, "file_form" : upload_file_form, "files": children_files, "path_to_root" : path_to_root, "path_quantity" : path_quantity,"paths_numbers":{"first" : 1, "secound":2, "penultimate":path_quantity-1, "last":path_quantity} })


@login_required(login_url="/user/login")
def folders (request) :
    # create a empty warn message to hove global acess inside this scope
    warn_message = ""

    folders = request.user.profile.folders.all()

    # return html page with necessary data
    return render (request, "dashboard/folders.html", {"folders" : folders})

@login_required(login_url="/user/login")
def files (request) :

    files = request.user.profile.files.all()

    # return html page with necessary data
    return render (request, "dashboard/files.html", {"files" : files})
