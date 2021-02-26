import os
import sys
import zipfile

import config


def backup():
    if count == 0:
        print("Setup config file \n Add to backup array 'path'")
    else:
        for x in config.backup:
            file_name = os.path.basename(x)
            backup_path_temp = backup_path + "/" +  file_name + ".zip"
            zipfile.ZipFile(backup_path_temp,mode='w').write(x)
            

count = len(config.backup)

if config.backup_path == "":
    backup_path = input("Backup path: ")
    backup()
else:
    backup_path = config.backup_path
    backup()





# for file in os.listdir("key/"):
#         if file.endswith(".key"):
#             print(file)