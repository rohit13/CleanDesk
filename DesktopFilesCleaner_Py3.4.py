import os
import sys
import shutil

def identify_file_mime_type(src_dir):
        for userFile in src_dir:
                if os.path.isdir(userFile):
                        continue
                else:
                        extension = userFile.split(".")[-1]
                        if extension in {'mp3','MP3','mp4','MP4','wma','WMA','mkv','MKV'}:
                                dest_dir="Entertainment"
                        elif extension in {'txt','TXT','doc','DOC','docx','DOCX','xlsx','XLSX','xls','XLS','pdf','PDF','log','LOG'}:
                                dest_dir="Docs"
                        elif extension in {'bmp','BMP','jpg','JPG','jpeg','JPEG','gif','GIF','png','PNG'}:
                                dest_dir="Images"
                        elif extension in {'exe','EXE'}:
                                dest_dir="Softwares"
                        elif extension in {'msg','MSG'}:
                                dest_dir="EMails"
                        else:
                                dest_dir="Others"
                        mov_file_to_folder(userFile, dest_dir)
        return

def mov_file_to_folder(userFile, dest_dir):
        if os.path.exists(dest_dir):
                shutil.move(userFile,dest_dir)
        else:
                os.mkdir(dest_dir)
                shutil.move(userFile,dest_dir)
        return

os.chdir(os.path.join(os.environ['USERPROFILE'], "Desktop"))
desktop = os.listdir(os.path.join(os.environ['USERPROFILE'], "Desktop"))
MINIMUM_DESKTOP_FILES = 1

print ("|---------------------------------------------------------------------|\n")
print ("This script will move all the files on your Desktop to their respective folders\n")
print ("based on their file type and make your Desktop clean in a matter of seconds.\n")
print ("|---------------------------------------------------------------------|\n")
print ("I know, I know, you need it. I Already started cleaning your Desktop.\n\n")
print ("|---------------------------------------------------------------------|\n")
print ("|-- Please look for following directory names on your desktop --|\n")
print ("|Entertainment, Docs, Images, Softwares, EMails, Others|\n")
print ("|---------------------------------------------------------------------|\n")

if len(desktop) >= MINIMUM_DESKTOP_FILES:
        try:
                identify_file_mime_type(desktop)
                print ("I moved the files homey. Your desktop is clean!\n")
                input("Press enter to exit.")

        except shutil.Error as e:
                print ("Sorry! I did not move some of your files\nas they already exists at destination.\n  %s") % e
                input("Press enter to exit.")
else: 
        print ("You're testing me, huh? I got you! There are no files to move. Bye!\n")
        input("Press enter to exit.")