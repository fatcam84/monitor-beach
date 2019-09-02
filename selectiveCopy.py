import os, shutil

os.chdir('C:\\Users\\Camer\\Downloads')
for filename in os.listdir():
    if filename.endswith('.zip'):
        shutil.move(filename, 'C:\\Users\\Camer\\Downloads\\zip_files')
