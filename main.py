#Blooket Bot Version 1.0.0 Public
#Created by Oliver Sproston
#Open Source, but you must credit me with any iterations. Currently not in exe form, but feel free to convert it.
#Requires pynput installed, to install run "pip install pynput" in cmd console. Requires PIP + IDLE python.
#Troubleshooting: If not working, open a tab in your browser before starting the program. Any questions, please contact me on discord: ItsPenguinCraft#5159.
import webbrowser
import pynput
import time
from pynput.keyboard import Key, Controller
from BotNames import *
keyboard = Controller()
restA = 7
i = 0
def start():
    if i == 0:
        #Gets requied user input
        id = input("WHAT IS THE GAME ID?")
        nameType = input("WHAT DO YOU WANT THE BOTS TO BE CALLED? Presets: \"rickroll\"")
        nameNum = 0
        #Finds presets
        if nameType == "rickroll" or "Rick Roll" or "Rick roll":
            name = rickroll.split()
        else:
            print("ERROR PRESET NOT FOUND")
            print("RESTARTING...")
            start()
        nameWords = len(name)
        while nameNum <= nameWords:
            #gets game code and opens website
            website = "https://www.blooket.com/play?id=" + id
            print("Opening website...")
            webbrowser.open(website)
            #simulates key presses
            time.sleep(restA)
            keyboard.type(name[nameNum])
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(restA / 1.5)
            keyboard.press(Key.ctrl)
            keyboard.press("w")
            keyboard.release(Key.ctrl)
            keyboard.release("w")
            nameNum = nameNum + 1
            time.sleep(0.3)
    elif i == 1:
            id = input("WHAT IS THE GAME ID?")
            nameNum = 0
            nameWords = len(customArray)
            while nameNum <= nameWords:
                #gets game code and opens website
                website = "https://www.blooket.com/play?id=" + id
                print("Opening website...")
                webbrowser.open(website)
                #simulates key presses
                time.sleep(restA)
                keyboard.type(customArray[nameNum])
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                time.sleep(restA / 1.5)
                keyboard.press(Key.ctrl)
                keyboard.press("w")
                keyboard.release(Key.ctrl)
                keyboard.release("w")
                nameNum = nameNum + 1
                time.sleep(0.3)
    elif i ==2:
            id = input("WHAT IS THE GAME ID?")
            nameWords = len(customArrayInv)
            nameNum = nameWords-1
            while nameNum >= 0:
                #gets game code and opens website
                website = "https://www.blooket.com/play?id=" + id
                print("Opening website...")
                webbrowser.open(website)
                #simulates key presses
                time.sleep(restA)
                keyboard.type(customArrayInv[nameNum])
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                time.sleep(restA/1.5)
                keyboard.press(Key.ctrl)
                keyboard.press("w")
                keyboard.release(Key.ctrl)
                keyboard.release("w")
                nameNum = nameNum -1
                time.sleep(0.5)
startChoice = input("HELLO! WHAT DO YOU WANT TO DO? YOU CAN START THE MAIN PROGRAM (start), YOU CAN CREATE YOUR OWN SENTENCE (custom) OR INVERT THE A CUSTOM SENTENCE (customInv)")
if startChoice == "start":
    
    start()
    print("COMPLETE")
elif startChoice == "custom":
    #Gets custom sentence
    custom = input("ENTER YOUR SENTENCE HERE:")
    customArray = custom.split()
    i = 1
    start()
else:
    #Gets custom sentence
    customInv = input("ENTER YOUR SENTENCE HERE")
    customArrayInv = customInv.split()
    i = 2
    start()