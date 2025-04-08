import os
import shutil

def move_file_to_folder():
    filename = input("Enter the file name to copy: ")
    folder = input("Enter the name of the folder to copy into: ")

    if not os.path.exists(filename):
        print("The file '" + filename + "' was not found.")
        return

    if not os.path.exists(folder):
        os.mkdir(folder)

    shutil.copy(filename, os.path.join(folder, filename))
    print("File copied to '" + folder + "' folder.")

move_file_to_folder()
