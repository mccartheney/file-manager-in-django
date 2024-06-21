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