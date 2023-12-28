import os


if os.path.exists("MyFolder-2"):
 print("Folder Exist")
 # os.rmdir("MyFolder-2")
else:
 os.mkdir("MyFolder-2")

 print("Created")


 # mkdir  is used to create folder
 # rmdir is to delete

 # os  - operating system 
