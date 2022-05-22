#importing the os module
# this programm check the names of the files and folders in teh same location 
# - only if they end with (p3) mp3 as it as and moves it to the 
# destination (a variable that has the target location inscribed)
import os
import shutil
import ntpath
#to get the current working directory
destination = "/Users/mac/Documents/Music/Clean mp3s"
def Returnallfiles(path):
    files = os.listdir(path)
    for file in files:
        if file == '.DS_Store' or file == "Check the Names of the Files.py":
            print(path)
            continue
        elif os.path.isdir(path + "/" + file):
                files = os.listdir(path)
                files.append(Returnallfiles(path + "/" + file))
        else:
            filereveersed = file [::-1]
            if (filereveersed[0] == '3' and filereveersed[1] == 'p'):
                source = path + "/" + file
                if not os.path.exists(destination + "/" + file):
                    shutil.move(source, destination)
    return files

directory = os.getcwd()
Returnallfiles(directory)
