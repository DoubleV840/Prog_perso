# -*- coding: utf-8 -*-
#Created by Willipatafoul at 15:54 on 12/05/2023
#
import pyautogui
import time
time.sleep(20)

def main():
    count = 0
    
    pyautogui.keyDown("shift")
    while count <= 100:
        pyautogui.typewrite("Chargement ")
        pyautogui.typewrite(str(count))
        pyautogui.press("%")
        pyautogui.press("enter")
        count = count+1
    pyautogui.keyUp("shift")
    
if __name__ == '__main__':
    main()
