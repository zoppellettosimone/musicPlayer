import random
import os
from pygame import mixer
import time
      
def Play():
    try:
        mixer.music.load(song)
        mixer.music.play()
        print(f"\nPlaying {listDir[r].lower()}")
    except:
        print("Error loading a song randomly")

def PlayName(nameSong):
    try:
        mixer.music.load(link+"\\"+nameSong)
        mixer.music.play()
        print(f"Playing {nameSong.lower()}")
    except:
        print("Error loading a specified song, please check its presence")

def Pause():
    try:
        mixer.music.pause()
    except:
        print("Error while pausing a song")

def Stop():
    try:
        mixer.music.stop()
    except:
        print("Error in stopping a song")

def Resume():
    try:
        mixer.music.unpause()
    except:
        print("Error resuming a song")

def LoadDir():
    linkInput = input("\nWhich folder are the songs in? ")

    try:
        os.chdir(linkInput)

        return linkInput
    except:
        print("Error in loading the folder, check its existence and its path")
        return LoadDir()

print('''

    MP3 Music Player by Console
    Written by Simone Zoppelletto

''')

link = LoadDir()
listDir = os.listdir()

mixer.init()

r = random.randint(0, len(listDir)-1)

song=f'{link}\\{listDir[r]}'

print(song)
print(f"Playing {listDir[r]}")

Play()

inputUser = ""
lastAction = "Play"

while(inputUser.lower() != "Exit"):
    print('''
            Write "Exit" to Exit
            Write "Stop" to stop the song
            Write "Resume" to resume a blocked song
            Write "Pause" to stop a song
            Write "Load" to load one randomly
            Write the exact name of the song if you want to upload a specific one (ending with .mp3)
        ''')

    inputUser = input("What do you want to do? ")

    if(inputUser.lower() == "stop"):
        if(lastAction == "Resume" or lastAction == "Play"):
            Stop()
            lastAction = "Stop"
        else:
            print("It is not possible to stop the song")
    elif(inputUser.lower() == "resume"):
        if(lastAction == "Stop" or lastAction == "Pause"):
            Resume()
            lastAction = "Resume"
        else:
            print("The song cannot be resumed")
    elif(inputUser.lower() == "pause"):
        if(lastAction == "Resume" or lastAction == "Play"):
            Pause()
            lastAction = "Pause"
        else:
            print("The song cannot be paused")
    elif(inputUser.lower() == "load" or inputUser.replace(' ','') == ""):
        
        listDir = os.listdir()
        lastr = r
        while(lastr == r):
            r = random.randint(0, len(listDir)-1)
        
        song=f'{link}\\{listDir[r]}'

        Play()

        lastAction = "Play"
    elif(inputUser.lower() == "Exit"):
        print("Thanks")
    elif(inputUser.lower().endswith(".mp3")):
        PlayName(inputUser)

        lastAction = "Play"
    else:
        print("Invalid Input: " + inputUser)
        if(inputUser.lower() == "play"):
            print("Do you mean Load?")



print("Music End")