import os
import shutil
import ntpath
import re
directory = os.getcwd()
files = os.listdir(directory)
for file in files: 
    name = file
    name = re.sub('#', ' ', name)
    os.rename(directory + "/" + file, directory + "/" + name)
