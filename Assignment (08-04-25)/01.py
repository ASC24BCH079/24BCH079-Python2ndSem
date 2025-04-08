import os
def name_count(filename,name):
    if not os.path.exists(filename):
        print("The file was not found. Check the name again.")
        return 0
    f=open(filename,'r')
    text=f.read()
    f.close()
    name=name.lower()
    text=text.lower()
    total=text.count(name)
    print("Your name appeared",total,"times")
    return total

file_name=input("Enter file name: ")
my_name=input("Enter your name: ")
name_count(file_name,my_name)
