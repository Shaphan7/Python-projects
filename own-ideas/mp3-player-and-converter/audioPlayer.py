import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
import subprocess
import shutil

def converter():
    choice = input("Song or Folder? ").upper().strip()
    if choice == "FOLDER":
        folder = input("Folder of Songs to Covert: ")
        if not os.path.isdir(folder):
            return print("Folder not found")
        songs = [song for song in os.listdir(folder) if song.endswith('.mp4')]
        if not songs:
            print("No songs to convert!")
        print("Processing...")
        for song in songs:
            subprocess.run(['ffmpeg', '-i', str(os.path.join(folder, song)), '-q:a', '0', '-map', 'a', f'{os.path.join(folder, os.path.splitext(song)[0])}.mp3'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"{song} has been Converted!")
    elif choice == "SONG":
        folder = input("Folder contain the Song to Covert: ")
        if not os.path.isdir(folder):
            return print("Folder not found")
        song = input("Song to Covert: ")
        if not os.path.isfile(os.path.join(folder, song)):
            return print("File not found")
        print("Processing...")
        subprocess.run(['ffmpeg', '-i', str(os.path.join(folder, song)), '-q:a', '0', '-map', 'a', f'{os.path.join(folder, os.path.splitext(song)[0])}.mp3'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"{song} has been Converted!")
    else:
        print("Invalid Command")

def moveSong(folder):
    old_folder = input("Old Folder: ").strip().upper()
    song_name = input("Song name: ").strip().upper()
    if not os.path.isfile(os.path.join(old_folder, song_name)):
        return print("Song not found")
    shutil.move(os.path.join(old_folder, song_name), folder)
    print("Song has been added successfully!")

def removeSong(folder):
    song_name = input("Song name: ").strip().upper()
    if not os.path.isfile(os.path.join(folder, song_name)):
        return print("Song not found")
    os.remove(os.path.join(folder, song_name))
    print("Song has been removed successfully!")

def playSong(song_name, folder, Loop=False, PlayAll=False, Songs=None):
    if PlayAll:
        index = 0
        print(len(Songs))
        while True:
            if index == len(Songs):
                index -= len(Songs)
            file_path = os.path.join(folder, Songs[index])
            current_song = Songs[index]
            index += 1
            print(index)
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                print(f"{current_song} is currently playing.")
                print("Use [P]ause, [U]npause, [N]ext, and [S]top")
                while True and pygame.mixer.music.get_busy():
                    command = input("> ").upper().strip()
                    if command == "S":
                        pygame.mixer.music.stop()
                        print("Song Stoped!")
                        return
                    elif command == "P":
                        pygame.mixer.music.pause()
                        print("Songs paused")
                    elif command == "N":
                        pygame.mixer.music.stop()
                        break
                    elif command == "U":
                        pygame.mixer.music.unpause()
                        print("Songs unpaused")
                    else:
                        print("Invalid Command!")
    else:
        file_path = os.path.join(folder, song_name)
        pygame.mixer.music.load(file_path)
        if Loop:
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.play()
        print(f"{song_name} is currently playing.")
        print("Use [P]ause, [U]npause, and [S]top")
        while True:
            command = input("> ").upper().strip()
            if command == "S":
                pygame.mixer.music.stop()
                print("Song Stoped!")
                return
            elif command == "P":
                pygame.mixer.music.pause()
                print("Songs paused")
            elif command == "U":
                pygame.mixer.music.unpause()
                print("Songs unpaused")
            else:
                print("Invalid Command!")

def getFolder():
    print("------------MP3-Player------------")
    folder_name = input("Folder Name: ").upper().strip()
    return folder_name

def songSelect(folder_name):
    # am aware that if you type the folder_name wrong it's quits the app
    if not os.path.isdir(folder_name):
        print(f"Folder '{folder_name}' not found!")
        return False
    songs = [song for song in os.listdir(folder_name) if song.endswith('.mp3')]
    print("Pick a Song to play:")
    for index, song in enumerate(songs, start=1):
        print(f"{index}. {song}")

    choice = input("> ")
    # Yes I know I am using int(choice) - 1 twice
    # I didn't think making a commands dict for only 3 commands was nessary
    if choice == "exit":
        return False
    elif choice == "add song":
        moveSong(folder_name)
    elif choice == "remove song":
        removeSong(folder_name)
    elif choice == "converter":
        converter()
    elif choice == "help":
        print("-----------Help-----------\n" \
              "exit = close program\n" \
              "converter = to access the converter\n" \
              "add song = add new song to existing folder\n" \
              "remove song = remove songs from existing folder\n")
    elif not choice.isdigit():
        print("Invalid choice")
    elif not 0 < int(choice) <= len(songs):
        print("Invalid choice")
    else:
        loopAll = input("Loop songs?(y/n)")
        if loopAll == "y":
            playSong(songs[int(choice) - 1], folder_name, PlayAll=True, Songs=songs)        
        else:
            loop = input("Loop song?(y/n)")
            if loop == "y":
                playSong(songs[int(choice) - 1], folder_name, Loop=True)        
            else:
                playSong(songs[int(choice) - 1], folder_name)
    

def main():
    folder_name = getFolder()
    # Keeping Playing if the user stops a song while it doesn't return false
    while songSelect(folder_name) != False:
        pass

if __name__ == "__main__":
    try:
        pygame.mixer.init()
    except pygame.error as e:
        print(f"Initilization Failed: {e}")
    main()
