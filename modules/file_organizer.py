import os
import shutil

class FileOrganizer:
    def organize_files(self):
        path = input("Enter folder path: ")

        for file in os.listdir(path):
            if "." in file:
                ext = file.split(".")[-1]
                folder = os.path.join(path, ext)
                os.makedirs(folder, exist_ok=True)
                shutil.move(os.path.join(path, file), folder)

        print("📁 Files organized successfully")
