import os
import shutil
# Project: file-organizer

FileTypes = {
    "Img": ['.png', '.jpg', '.ico'],
    "Document": ['.txt', '.json', '.cvs', '.pdf'],
    "App": ['.py', '.html', '.js', '.css', '.c++', '.c', '.cs', '.php', '.ru', '.java', '.exe'],
    "Video": ['.mp4'],
    "Audio": ['.mp3']
}

def sortFile(fileName, ext, typeName):
    file = fileName + ext
    if os.path.isdir(typeName):
        try:
            shutil.move(file, f"./{typeName}")
        except shutil.Error as e:
            if "already exists" in str(e):
                print(f"Skipping {fileName} since it already exists!")
            else:
                raise e
    else:
        print(f"{typeName} not found")
        print(f"creating {typeName} folder!")
        os.makedirs(typeName)
        try:
            shutil.move(file, f"./{typeName}")
        except shutil.Error as e:
            if "already exists" in str(e):
                print(f"Skipping {fileName} since it already exists!")
            else:
                raise e

itemsInCurrent_d = os.listdir()
for item in itemsInCurrent_d:
    if os.path.isfile(item):
        fileName, ext = os.path.splitext(item)
        for name, exts in FileTypes.items():
            if ext in exts:
                sortFile(fileName, ext, name)
                break
        else:
           sortFile(fileName, ext, "ETC")
