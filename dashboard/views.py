# render and redirect to render a page or redirect user to other page
from django.shortcuts import render, redirect

# import folder model to manage folders
from .models import folder

# import uuid to create unique random ids
from uuid import uuid4

# import login required to make pages login required
from django.contrib.auth.decorators import login_required

# import file_form to upload files
from .forms import file_form

# import file models to create a file model
from .models import file

# import utils to uset utils functions
import utils

# view to homepage to dashboard
@login_required(login_url="/user/login")
def home_dashboard (request) :

    if request.user.is_staff or request.user.is_superuser :
        return redirect ("/admin/")

    print(request.user.profile.max_storage)

    # get all files and folder
    all_files = request.user.profile.files.all()
    all_folders = reversed(request.user.profile.folders.all())


    # create context to send to html page (front end)
    context = {
        'all_files' : all_files,
        'file_sizes' : utils.get_type_files_size(all_files=all_files),
        'file_types' : utils.get_file_types(),
        'used_storage' : utils.get_used_storage(all_files=all_files),
        'total_storage' : request.user.profile.max_storage,
        'used_porcentage' : utils.get_used_porcentage(all_files),
        'used_float_porcentage': utils.get_used_float_porcentage(all_files),
        'left_porcentage' : utils.get_left_porcentage(all_files),
        'folders' : all_folders,
        "files" : utils.get_files_attributes(all_files)
    }

 
    # render home page
    return render (request, "dashboard/index.html", context)

# view to file manager (on root folder)
@login_required(login_url="/user/login")
def file_manager_dashboard (request) :

    if request.user.is_staff or request.user.is_superuser :
        return redirect ("/admin/")

    # get root folder (main folder, where all is inside and cannot be deleted), and her name
    root_folder = request.user.profile.folders.all().filter(parent_folder = None).filter(folder_name="root")[0]
    children_files = root_folder.children_files.all()

    # get all folders inside root folder
    folders = root_folder.children_folder.all()
    if folders : # if have folders, invert them
        folders = reversed(folders)

    # form to upload files
    upload_file_form = file_form()


    # create context to send to html page (front end)
    context =  {
        "folders" : folders, 
        "folder_name" : root_folder.folder_name, 
        "file_form" : upload_file_form, 
        "files": children_files,
        "warn_message" : ""
    }

    if request.method == "POST" : # if user send something

        # get user and user profile to link the file or the folder to them  
        user = request.user
        user_profile = user.profile

        if request.POST.get("file_to_remove") :

            # get folder to delete
            id_file_to_delete = request.POST.get("file_to_remove")
            folder_to_delete = children_files.filter(file_id = id_file_to_delete)[0]

            # delete all folders
            folder_to_delete.delete()

            # refresh folders
            folders = root_folder.children_folder.all()
            folders = reversed(folders)

            # update context
            context["folders"] = folders
            context["files"] = root_folder.children_files.all()

            # return html page with necessary data
            return render (request, "dashboard/fileManagerRoot.html",context)

        if request.POST.get("folder_to_rename") : # if the user send a new name to a folder

            # get folder to rename
            folder_id_to_rename = request.POST.get ("folder_id_to_rename")
            folder_to_rename = user_profile.folders.all().filter(folder_id = folder_id_to_rename)[0]

            # get folders with same name
            folder_with_the_same_name = root_folder.children_folder.all().filter(folder_name = request.POST.get("folder_to_rename"))

            if folder_with_the_same_name: # if have folders with same name

                # update warn message
                context["warn_message"] = "You already have folders with that name, try other name"

                # return html page with necessary data
                return render (request, "dashboard/fileManagerRoot.html", context)

            # rename that folder
            folder_to_rename.folder_visible_name = request.POST.get("folder_to_rename")
            folder_to_rename.folder_name = request.POST.get("folder_to_rename")

            # save the changes
            folder_to_rename.save()

            # refresh folders
            folders = root_folder.children_folder.all()
            folders = reversed(folders)

            # update context
            context["folders"] = folders
            context["files"] = root_folder.children_files.all()

            # return html page with necessary data
            return render (request, "dashboard/fileManagerRoot.html",context)


        elif request.POST.get("folder_to_remove"): # if user send a folder to remove

            # get folder to delete
            folder_id_to_delete = request.POST.get("folder_to_remove")
            folder_to_delete = user_profile.folders.all().filter(folder_id = folder_id_to_delete)

            # delte that folder
            folder_to_delete.delete()

            # get all folders inside root folder
            folders = root_folder.children_folder.all()
            folders = reversed(folders)

            # update context
            context["folders"] = folders
            context["files"] = root_folder.children_files.all()

            # return html page with necessary data
            return render (request, "dashboard/fileManagerRoot.html",context)

        elif request.POST.get("folder_input"): # if user send a folder to create

            # get the name of the new folder
            folder_name = request.POST.get("folder_input")
            folder_visible_name = request.POST.get("folder_input")

            # get how many folder with the same name exists
            exists_folder_with_same_name = root_folder.children_folder.all().filter(folder_name = folder_name)

            if exists_folder_with_same_name : # if exist any folder with the same name
                # add (1) or the quantity of folders wit the same name, on front of the name
                folder_visible_name = f'{folder_name} ({len(exists_folder_with_same_name)})'

            # create the new folder
            new_folder = folder.objects.create(
                User = user_profile,
                folder_name = folder_name,
                folder_id = uuid4(),
                parent_folder = root_folder,
                folder_visible_name = folder_visible_name
            )

            # refresh folders
            folders = root_folder.children_folder.all()
            folders = reversed(folders)

            # update context
            context["folders"] = folders
            context["files"] = root_folder.children_files.all()

            # return html page with necessary data
            return render (request, "dashboard/fileManagerRoot.html",context)
        
        else : # if user send file

            # get file infos
            file_from_user =request.FILES["files"]
            file_name_from_user = str(request.FILES["files"])
            visible_file_name_from_user = str(request.FILES["files"])

            # get all files with the same name
            file_with_same_name = children_files.filter(file_name = file_name_from_user)

            # if have file with same name do the same as folder
            if file_with_same_name :
                visible_file_name_from_user = f"{file_name_from_user} ({len(file_with_same_name)})"
            
            file_size = round(file_from_user.size / (1024*1024) , 2)

            used_storage = utils.get_used_storage(request.user.profile.files.all())
            max_storage = request.user.profile.max_storage

            if (used_storage+file_size) > max_storage :
                context["warn_message"] = "You reached ypur limite, delete some file to upload that one"

                return render (request, "dashboard/fileManagerRoot.html",context)

            # create file
            new_file = file.objects.create(
                User = user_profile,
                file = file_from_user,
                file_id = uuid4(),
                file_visible_name = visible_file_name_from_user,
                file_name = file_name_from_user,
                parent_folder = root_folder
            )


            # update context
            context["files"] = root_folder.children_files.all()

            # return html page with necessary data
            return render (request, "dashboard/fileManagerRoot.html",context)

    # return html page with necessary data
    return render (request, "dashboard/fileManagerRoot.html", context)

# view to file manager (not on root folder)
@login_required(login_url="/user/login")
def file_manager_folder_dashboard (request, slug) :

    if request.user.is_staff or request.user.is_superuser :
        return redirect ("/admin/")


    # get folder id by slug (paremeter from url)
    folder_id = slug

    # get user profile (folders are connected to them) 
    user_profile = request.user.profile


    # get actual folder and folder name by id
    this_folder = request.user.profile.folders.all().filter(folder_id = folder_id)[0]
    
    # check if this folder exists, if dont redirect to homepage
    if len(request.user.profile.folders.all().filter(folder_id = folder_id)) == 0:
        return redirect("/dashboard/filemanager/")

    # check if this folder is root, if it is redirect to homepage
    if this_folder.parent_folder == None :
        return redirect("/dashboard/filemanager/")

    # get actual folder name
    this_folder_name = this_folder.folder_name

    # get root_folder
    root_folder = request.user.profile.folders.all().filter(parent_folder = None, folder_name="root").first()

    # get path to root
    path_to_root = utils.get_path_to_root(this_folder, root_folder)["path"]
    path_quantity = utils.get_path_to_root(this_folder, root_folder)["lenght"]

    # get all folders
    folders = this_folder.children_folder.all()

    # form to create a file
    upload_file_form = file_form()

    # get a parent id to go to them on press return button
    parent_id = this_folder.parent_folder.folder_id

    if this_folder.parent_folder.parent_folder == None : # root folder
        parent_id = ""

    # get folder files
    children_files = this_folder.children_files.all()

    # create context to send to html page (front end)
    context = {
        "folders":folders,
        "folder_id" : this_folder.folder_id, 
        "folder_name" : this_folder_name, 
        "parent_id":parent_id, 
        "file_form" : upload_file_form, 
        "files": children_files, 
        "path_to_root" : path_to_root, 
        "path_quantity" : path_quantity,
        "paths_numbers":{
            "first" : 1, 
            "secound":2, 
            "penultimate":path_quantity-1, 
            "last":path_quantity
        },
        "warn_message" : ""
    }


    if (request.method == "POST") : # if user sent something 
        if request.POST.get("file_to_remove") :
            
            # get file to remove
            id_file_to_delete = request.POST.get("file_to_remove")
            file_to_delete = children_files.filter(file_id = id_file_to_delete)[0]

            # remove file
            file_to_delete.delete()

            # refresh files
            children_files = this_folder.children_files.all()

            # update context
            context["files"] = children_files

            # return html page with necessary data
            return render (request, "dashboard/fileManagerFolder.html", context)



        if request.POST.get("folder_to_rename") : # if user send a folder to rename

            # get folder to rename
            folder_id_to_rename = request.POST.get ("folder_id_to_rename")
            folder_to_rename = user_profile.folders.all().filter(folder_id = folder_id_to_rename)[0]

            # get folder with same name
            folder_with_the_same_name = this_folder.children_folder.all().filter(folder_name = request.POST.get("folder_to_rename"))


            if folder_with_the_same_name: # if have folders with same name

                # refresh folders
                folders = this_folder.children_folder.all()
                folders = reversed(folders)

                # update context
                context["folders"] = folders
                context["warn_message"] = "You already have folders with that name, try other name"

                # return html page with necessary data
                return render (request, "dashboard/fileManagerRoot.html", context)

            # rename thet folder
            folder_to_rename.folder_visible_name = request.POST.get("folder_to_rename")
            folder_to_rename.folder_name = request.POST.get("folder_to_rename")

            # save the changes
            folder_to_rename.save()

            # refresh folders
            folders = this_folder.children_folder.all()
            folders = reversed(folders)

            # update context
            context["folders"] = folders

            # return html page with necessary data
            return render (request, "dashboard/fileManagerFolder.html", context)


        if request.POST.get("folder_to_remove"): # if user send a folder to remove
            

            # get id folder
            folder_id_to_delete = request.POST.get("folder_to_remove")
            # get folder by id
            folder_to_delete = folders.filter(folder_id = folder_id_to_delete)

            # delete that folder
            folder_to_delete.delete()
            folders = this_folder.children_folder.all()

            context["folders"] = folders

            # return html page with necessary data

            return render (request, "dashboard/fileManagerFolder.html", context)

        
        elif request.POST.get("folder_input") :# get folder name to create

            # get new  folder info
            folder_name = request.POST.get("folder_input")
            folder_visible_name = request.POST.get("folder_input")

            # get all folders inside the actual folder to see if have the same name as the new one
            exists_folder_with_same_name = this_folder.children_folder.all().filter(folder_name = folder_name)

            if exists_folder_with_same_name : # if have a folder with the same name
                # add the quantity of folders in front
                folder_visible_name = f'{folder_name} ({len(exists_folder_with_same_name)})'
                

            # create folder
            new_folder = folder.objects.create(
                User = user_profile,
                folder_name = folder_name,
                folder_id = uuid4(),
                parent_folder = this_folder,
                folder_visible_name = folder_visible_name
            )

            # refresh folders
            folders = this_folder.children_folder.all()

            # update context
            context["folders"] = folders

            # return html page with necessary data
            return render (request, "dashboard/fileManagerFolder.html", context)
        else : # if uder send a file
            # get new file info
            file_from_user =request.FILES["files"]
            file_name_from_user = str(request.FILES["files"])
            visible_file_name_from_user = str(request.FILES["files"])

            # get files with the same name
            file_with_same_name = children_files.filter(file_name = file_name_from_user)

            # if have folder with same name, do the same as folders
            if file_with_same_name :
                visible_file_name_from_user = f"{file_name_from_user} ({len(file_with_same_name)})"

            file_size = round(file_from_user.size / (1024*1024) , 2)

            used_storage = utils.get_used_storage(request.user.profile.files.all())
            max_storage = request.user.profile.max_storage

            if (used_storage+file_size) > max_storage :
                context["warn_message"] = "You reached ypur limite, delete some file to upload that one"

                return render (request, "dashboard/fileManagerFolder.html", context)


            # create files
            new_file = file.objects.create(
                User = user_profile,
                file = file_from_user,
                file_id = uuid4(),
                file_visible_name = visible_file_name_from_user,
                file_name = file_name_from_user,
                parent_folder = this_folder
            )

            # update context
            context["files"] = children_files

            # return html page with necessary data
            return render (request, "dashboard/fileManagerFolder.html", context)

    # return html page with necessary data
    return render (request, "dashboard/fileManagerFolder.html", context)


@login_required(login_url="/user/login")
def folders (request) :

    if request.user.is_staff or request.user.is_superuser :
        return redirect ("/admin/")


    # get all folders
    folders = request.user.profile.folders.all()

    # create context
    context = {
        "folders" : folders
    }

    # return html page with necessary data
    return render (request, "dashboard/folders.html", context)

@login_required(login_url="/user/login")
def files (request) :

    if request.user.is_staff or request.user.is_superuser :
        return redirect ("/admin/")


    # get all files
    files = request.user.profile.files.all()

    # create context
    context = {
        "files" : files
    }

    # return html page with necessary data
    return render (request, "dashboard/files.html", context)
