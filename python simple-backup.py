import os
import shutil

file_name = input("Enter file name: ")

if os.path.exists(file_name):
    shutil.copy(file_name, "backup.txt")
    print("Backup done")
else:
    print("File not found")
