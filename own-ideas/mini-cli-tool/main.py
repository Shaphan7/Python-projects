import os
import shutil

# Project: mini-cli-tool

#---------Functions---------#
def doesFileExist():
    file = input("name: ")
    return os.path.exists(file)
def makeNewFolder():
    name = input("Folder name: ")
    try:
        os.makedirs(name)
    except FileExistsError:
        return f"{name} already exists"
    return "Command executed!"
def rename():
    oldName = input("Previous name: ")
    newName = input("New name: ")
    try:
        os.rename(oldName, newName)
    except FileNotFoundError:
        return "File/Folder not Found!"
    return "File/Folder Renamed Successfully!"
def deleteFile():
    name = input("Name of File (example 'index.html'): ")
    if not os.path.isfile(name):
        return "File not Found!"
    confirmation = input("Are you sure? (y/n): ")
    if confirmation == "y":
        os.remove(name)
        return f"{name} has been removed successfully!" 
    else:
        return "Process stopped!"
def deleteFolder():
    name = input("Name of Folder: ")
    if not os.path.isdir(name):
        return "Folder not Found!"
    confirmation = input("Are you sure? (y/n): ")
    if confirmation == "y":
        try:
            os.rmdir(name)
        except OSError:
            folderNotempty = input("Folder is not Empty still Continue? (y/n)")
            if folderNotempty == "y":
                shutil.rmtree(name)
            else:
                return "Process stopped!"
        return f"{name} has been removed successfully!" 
    else:
        return "Process stopped!"
def changeDirectory():
    newDirectory = input("New directory: ")
    try:
        os.chdir(newDirectory)
    except FileNotFoundError:
        return "Directory not found!"
    return f"Location changed to '{newDirectory}'"
def copy():
    file = input('File name: ')
    destinationfolder = input('Destination folder: ')
    try:
        shutil.copy(file, destinationfolder)
        return f"copied {file} to {destinationfolder} successfully!"
    except FileNotFoundError:
        return "File/Folder not Found"
def move():
    file = input('File name: ')
    destinationfolder = input('Destination folder: ')
    try:
        shutil.move(file, destinationfolder)
        return f"moved {file} to {destinationfolder} successfully!"
    except FileExistsError:
        return f"{file} already exists"
    except FileNotFoundError:
        return "File/Folder not Found"

commands = {
    "location": lambda: print(f"Current Directory: {os.getcwd()}"),
    "la": lambda: print(f"Things in current Directory: {os.listdir()}"),
    "find": lambda:  print(doesFileExist()),
    "mnd": lambda: print(makeNewFolder()),
    "rename": lambda: print(rename()),
    "copy": lambda: print(copy()),
    "move": lambda: print(move()),
    "d_file": lambda: print(deleteFile()),
    "d_folder": lambda: print(deleteFolder()),
    "cd": lambda: print(changeDirectory()),
    "help": lambda: print("-------------------Help------------------\n"
                          "la = list all item in current directory\n" \
                          "mnd = make new directory\n" \
                          "rename = rename a file or folder\n" \
                          "d_file = delete a file\n" \
                          "d_folder = delete a folder\n" \
                          "copy = copy a file in a folder\n"
                          "move = move a file in a folder\n"
                          "cd = change directory\n" \
                          "exit = close app\n" \
                          "-----------------------------------------")
}

#---------Main-Loop---------#
def main():
    while True:
        command =  input("Command: ")
        if command in commands:
            commands[command]()
        elif command == "exit":
            print("App closed")
            break
        else:
            print("The syntax of the command is incorrect! (use 'exit' or 'help')")

main()
