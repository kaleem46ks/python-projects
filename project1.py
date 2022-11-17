import os, shutil

# Note: you can write every single extension inside tuple
dict_extension ={
'audio_extensions' : ('.mp3', '.m4a', '.wav', '.flac'),
'videos_extensions' : ('.mp4', '.mkv', '.MKV', '.flv', '.mpeg'),
'documents_extensions' : ('.doc', '.pdf', '.txt')
}

folderpath = input('input folder path: ')

def file_finder(folder_path,file_extension):
    # files = []
    # for file in os.listdir(folderpath):
    #     for extension in file_extension:
    #         if file.endswith(extension):
    #             files.append(file)
    # return files
    return [file for file in os.listdir(folderpath) for extension in file_extension if file.endswith(extension)]

# print(file_finder(folderpath,videos_extensions))
for extension_type,extension_tuple in dict_extension.items():
    folder_name = extension_type.split('_')[0]+'Files'
    folder_path = os.path.join(folderpath, folder_name)
    if os.path.exists(folder_path):
        pass
    else:        
        os.mkdir(folder_path)
    # os.mkdir(folder_path)
    for item in (file_finder(folderpath,extension_tuple)):
        item_path = os.path.join(folderpath,item)
        item_new_path = os.path.join(folder_path,item)
        shutil.move(item_path,item_new_path)

    # print('calling file finder')
    # print(file_finder(folderpath,extension_tuple))

    # for i in os.listdir(folderpath):
    #     if i.endswith(ext_tuple):
    #         if os.path.exists(folder_path):
    #             pass
    #         else:        
    #             os.mkdir(folder_path)