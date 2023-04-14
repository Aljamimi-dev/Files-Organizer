import sys
import fnmatch
import os
import shutil
import pathlib

if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

#temp_path = os.path.dirname(sys.executable)
path = pathlib.PureWindowsPath(fr'{application_path}').as_posix()
all_files = list()
extension = set()

#list of all the files and extensions
for entry in os.scandir(path):
    if entry.is_file() and not fnmatch.fnmatch(entry, '*.ini'):
        all_files.append(entry.name)
        extension.add(os.path.splitext(entry)[1])

#creating the folders
for folder in extension:
    try:
        folder_path = path+'/All_'+folder[1:]+'s/'
        #creating the folder
        os.mkdir(folder_path)
        #check in the list of the files
        for file in all_files:
            if file.endswith(folder):
                #moving the file from the current directory to the directory
                shutil.move(path+'/'+file, folder_path+file)
    except FileExistsError:
        #if the folder already exists move the files to that folder
        for file in all_files:
            if file.endswith(folder):
                #moving the file from the current directory to the directory
                shutil.move(path+'/'+file, folder_path+file)
