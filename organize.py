import os
import shutil
from_dir = "/Users/dasfam/Downloads"
to_dir = "/Users/dasfam/Document_files"
listOfFiles = os.listdir(from_dir)

for file_name in listOfFiles:
   name, extension = os.path.splitext(file_name)
 #  print(name)
 #  print(extension)

   if extension == '':
      continue
   if extension in ['.txt', '.doc', '.docx', '.pdf']:
    path1 = from_dir + '/' + file_name
    path2 = to_dir + '/' + "Image_Files"
    path3 = to_dir + '/' + "Image_Files" + file_name
    print(path3)

    if os.path.exists(path2):
       print("moving"+ file_name + "...")
       shutil.move(path1,path3)
    else:
       os.makedirs(path2)
       print("moving"+ file_name + "...")
       shutil.move(path1,path3)

   
