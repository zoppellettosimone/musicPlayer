import random
import os
from pygame import mixer
import time
from datetime import datetime
      
def Play():
    try:
        mixer.music.load(song)
        mixer.music.play()
        print(f"\n[{datetime.now()}] Playing {listDir[r].lower()}")
    except:
        print(f"\n[{datetime.now()}] Error loading a song randomly")

def PlayName(nameSong):
    try:
        mixer.music.load(link+"\\"+nameSong)
        mixer.music.play()
        print(f"\n[{datetime.now()}] Playing {nameSong.lower()}")
    except:
        print(f"\n[{datetime.now()}] Error loading a specified song, please check its presence")

def Pause():
    try:
        mixer.music.pause()
        print(f"\n[{datetime.now()}] Pause")
    except:
        print(f"\n[{datetime.now()}] Error while pausing a song")

def Stop():
    try:
        mixer.music.stop()
        print(f"\n[{datetime.now()}] Stop")
    except:
        print(f"\n[{datetime.now()}] Error in stopping a song")

def Resume():
    try:
        mixer.music.unpause()
        print(f"\n[{datetime.now()}] Resume")
    except:
        print(f"\n[{datetime.now()}] Error resuming a song")

def LoadDir():
    linkInput = input(f"\n[{datetime.now()}] Which folder are the songs in? ")

    try:
        os.chdir(linkInput)

        return linkInput
    except:
        print(f"\n[{datetime.now()}] Error in loading the folder, check its existence and its path")
        return LoadDir()

print(f'''

    MP3 Music Player by Console
    Written by Simone Zoppelletto

''')

link = LoadDir()
listDir = os.listdir()

mixer.init()

r = random.randint(0, len(listDir)-1)

song=f'{link}\\{listDir[r]}'

print(f"\n[{datetime.now()}] {song}")

Play()

inputUser = ""
lastAction = "Play"

while(inputUser.lower() != "Exit"):
    print(f'''
            Write "Exit" to Exit
            Write "Stop" to stop the song
            Write "Resume" to resume a blocked song
            Write "Pause" to stop a song
            Write "Load" to load one randomly
            Write "cd directoryCompletePath" to change directory in a new directoryCompletePath
            Write the exact name of the song if you want to upload a specific one (ending with .mp3)
        ''')

    inputUser = input(f"\n[{datetime.now()}] What do you want to do? ")

    if(inputUser.lower() == "stop"):
        if(lastAction == "Resume" or lastAction == "Play"):
            Stop()
            lastAction = "Stop"
        else:
            print(f"\n[{datetime.now()}] It is not possible to stop the song")
    elif(inputUser.lower() == "resume"):
        if(lastAction == "Stop" or lastAction == "Pause"):
            Resume()
            lastAction = "Resume"
        else:
            print(f"\n[{datetime.now()}] The song cannot be resumed")
    elif(inputUser.lower() == "pause"):
        if(lastAction == "Resume" or lastAction == "Play"):
            Pause()
            lastAction = "Pause"
        else:
            print(f"\n[{datetime.now()}] The song cannot be paused")
    elif(inputUser.lower() == "load" or inputUser.replace(' ','') == ""):
        
        listDir = os.listdir()
        lastr = r
        while(lastr == r):
            r = random.randint(0, len(listDir)-1)
        
        song=f'{link}\\{listDir[r]}'

        Play()

        lastAction = "Play"
    elif(inputUser.lower() == "Exit"):
        print(f"\n[{datetime.now()}] Thanks")
    elif(inputUser.lower().endswith(".mp3")):
        PlayName(inputUser)

        lastAction = "Play"
    elif(inputUser.startswith("cd ")):
        newFolder = inputUser.lower()[3:]
        
        try:
            os.chdir(newFolder)
            print(f"\n[{datetime.now()}] Directory Changed")

            link = newFolder
            listDir = os.listdir()

            r = random.randint(0, len(listDir)-1)
            song=f'{link}\\{listDir[r]}'

            Stop()
            Play()
        except:
            print(f"Error with {newFolder}")
    
    else:
        print(f"\n[{datetime.now()}] Invalid Input: " + inputUser)
        if(inputUser.lower() == "play"):
            print(f"\n[{datetime.now()}] Do you mean Load?")



print(f"\n[{datetime.now()}] Music End")