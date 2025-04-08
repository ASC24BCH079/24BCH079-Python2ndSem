import os
import shutil

def copy_to_subfolder():
    src = 'testfile.txt'
    new_folder = 'copied_here'

    if not os.path.exists(new_folder):
        os.mkdir(new_folder)

    shutil.copy(src, new_folder + '/' + src)
    print('Copied successfully')

copy_to_subfolder()
