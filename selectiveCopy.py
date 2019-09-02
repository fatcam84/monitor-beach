"""
    This program will search a given directory for files with desired suffix and move them all to a different directory.
    In this example, I am searching my 'Downlaods' folder and moving all the .zip files to a folder called 'zip_files'.
"""

import os, shutil

os.chdir('C:\\Users\\Camer\\Downloads')
for filename in os.listdir():
    if filename.endswith('.zip'):
        shutil.move(filename, 'C:\\Users\\Camer\\Downloads\\zip_files')
