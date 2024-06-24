from django.shortcuts import render,redirect

def get_type_files_size (all_files): 
    file_types = {
        "images":[],
        "videos":[],
        "audios":[],
        "documents":[],    
    }

    type_sizes = {
        "images":[],
        "videos":[],
        "audios":[],
        "documents":[], 
    }

    for file in all_files :
        file_size = round(file.file.size / (1024*1024) , 2)
        file_extension = file.file_name.split('.')[-1].lower()

        if file_extension == "jpeg" or file_extension == "jpg" or file_extension == "png" or file_extension == "svg" :
            file_types["images"].append(file_size)
        elif file_extension == "mp3" :
            file_types["audios"].append(file_size)
        elif file_extension == "mp4" :
            file_types["videos"].append(file_size)
        else : 
            file_types["documents"].append(file_size)
        
    for file_type in file_types:
        total_size = sum(file_types[file_type])
        type_sizes[file_type] = total_size
        
    return type_sizes

def get_file_types () :
    return [
        "images",
        "videos",
        "audios",
        "documents",
    ]

def get_used_storage(all_files) :
    return round(sum(get_type_files_size(all_files=all_files).values()),2)

def get_total_storage () :
    return 50

def get_used_porcentage (all_files) :
    print(round((get_used_storage(all_files=all_files)/get_total_storage()) * 100))
    return round((get_used_storage(all_files=all_files)/get_total_storage()) * 100)

def get_used_float_porcentage (all_files ) :
    return round((get_used_storage(all_files=all_files)/get_total_storage()) * 100,2)

def get_left_porcentage (all_files) :
    return round(100 - get_used_float_porcentage(all_files),2)

def get_path_to_root (actual_folder, root_folder) :
    path_to_root = []
    path_quantity = 0
    root_folder = root_folder
    actual_folder_search = actual_folder
    actual_parent_folder = actual_folder_search.parent_folder

    while True :
        path_quantity += 1
        path_to_root
        path_to_root.append(actual_folder_search)
        
        if actual_folder_search == root_folder :
            path_to_root = reversed(path_to_root)
            break

        actual_folder_search = actual_parent_folder
        actual_parent_folder = actual_folder_search.parent_folder

    return {
        "path" : path_to_root,
        "lenght" : path_quantity
    }

def get_files_attributes (files) :
    files_attributes = []

    for file in files :
        file_size = round(file.file.size / (1024*1024) , 2)
        file_extension = file.file_name.split('.')[-1].lower()

        file_attribute = {
            "file_url" : file.file.url,
            "file_name" : file.file_visible_name,
            "file_extendion" : file_extension,
            "file_size" : file_size
        }

        files_attributes.append(file_attribute)

    return files_attributes
