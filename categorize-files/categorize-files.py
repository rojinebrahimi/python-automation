from os import path
import os
import shutil
from pathlib import Path

# -- Defined categories --------------------------------------------------------------------------------
categories = ['Documents', 'Pictures', 'Music', 'Videos', 'Compressed', 'Programmes']

# -- Defined extensions --------------------------------------------------------------------------------
documents = ['.pdf', '.docx', '.xlsx', '.pptx', '.epub', '.odx', '.srt', '.odt', '.txt', '.doc', '.ttf', '.ppt', '.crt']
pictures = ['.jpg', '.jpeg', '.png', '.svg']
music = ['.mp3']
videos = ['.mp4', '.mkv', '.wmv', '.mov', '.flv', '.avi', '.webm']
compressed = ['.zip', '.tar', '.rar', '.tar.gz', '.tar.xz']
programme_files = ['.yaml', '.yml', '.ovpn', 'apk', '.sh', '.py', '.java', '.class', '.exe', '.deb', '.rpm', '.ipynb', '.msi', '.vsix', '.xml', '.json', '.asm', '.pkl']

# -- Directory path ------------------------------------------------------------------------------------
dir_path = input("Enter the path of the directory you with to categorize its contents: ")


# -- Makes directories based on defined categories -----------------------------------------------------
def make_directories(source_dir, categories_list):
    for item in categories_list:
        if not os.path.exists(source_dir + '/' + item):
            new_directory = source_dir + '/' + item
            Path(new_directory).mkdir(parents=True, exist_ok=True)


# -- Print statement -----------------------------------------------------------------------------------
def move_announcement():
    return f"\n{'📗'} Files were moved to the new directory."


# -- Checks if the file exists -------------------------------------------------------------------------
def file_exists(file_name, path):
    files_list = os.listdir(path)
    if file_name in files_list:
        return True
    return False


# -- Moves files into their related directories --------------------------------------------------------
def fill_directories(source_path):
    file_names_list = os.listdir(source_path)
    for file in file_names_list:
        filename, file_extension = os.path.splitext(file)
        if file_extension in documents and not (file_exists(file, source_path + '/Documents')):
            shutil.move(os.path.join(source_path, file), source_path + "/Documents")
            print("Documents: ", move_announcement())
        elif file_extension in pictures and not (file_exists(file, source_path + '/Pictures')):
            shutil.move(os.path.join(source_path, file), source_path + "/Pictures")
            print("Pictures: ", move_announcement())
        elif file_extension in music and not (file_exists(file, source_path + '/Music')):
            shutil.move(os.path.join(source_path, file), source_path + "/Music")
            print("Music: ", move_announcement())
        elif file_extension in videos and not (file_exists(file, source_path + '/Videos')):
            shutil.move(os.path.join(source_path, file), source_path + "/Videos")
            print("Videos: ", move_announcement())
        elif file_extension in compressed and not (file_exists(file, source_path + '/Compressed')):
            shutil.move(os.path.join(source_path, file), source_path + "/Compressed")
            print("Compressed: ", move_announcement())
        elif file_extension in programme_files and not (file_exists(file, source_path + '/Programmes')):
            shutil.move(os.path.join(source_path, file), source_path + "/Programmes")
            print("Programmes: ", move_announcement())
        elif file_extension == "":
            pass
        else:
            print(f"\n{'📙'} Some files/folders are left because no match was found or they were duplicates.")


# -- Main flow -----------------------------------------------------------------------------------------
if path.exists(dir_path):
    make_directories(dir_path, categories)
    fill_directories(dir_path)
else:
    print(f"\n{'🛑'} Please enter the path correctly. Exiting... ")
    exit()
