import requests
import json
import os
import pyautogui

pyautogui.FAILSAFE = False

URL_TO_ESP32_DOOR_STATUS = ""

def get_door_status():
    return json.loads(requests.get(URL_TO_ESP32_DOOR_STATUS).text)["door_open"]

created_new_desktop = False

try:
    while True:
        if(get_door_status()):
            while(get_door_status()):
                os.system("nircmd mutesysvolume 1")
                if(created_new_desktop == False):
                    pyautogui.hotkey("win", "ctrl", "d")
                    created_new_desktop = True
                else:
                    pyautogui.hotkey("win", "ctrl", "right")
            pyautogui.hotkey("win", "ctrl", "left")
            os.system("nircmd mutesysvolume 0")
except:
    if(created_new_desktop == True):
        pyautogui.hotkey("win", "ctrl", "right")
        pyautogui.hotkey("win", "ctrl", "f4")
