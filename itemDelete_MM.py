'''
This script relies on a csv file containing the relevant information being accessible to the runtime user,
and a valid meditech user name capabable of running the required routine. 
Environment will need python 3.8 and pyautogui installed for this to work.
'''
import pyautogui
import os
import csv
import getpass

#csv code
def itemList():
    r = input("Enter file path: ")
    if not os.path.exists(r):
        print("Invalid path, please specify a different path")

    with open(r) as csvFile:
        list = []
        items = csv.reader(csvFile, delimiter=',')
        for item in items:
            list.append(item[0])
    return list

items = itemList()

userName = input("Enter Meditech Username: ")
passWord = getpass.getpass("Enter Meditech Password: ")

#get current screen size to determine where the 
size = tuple(pyautogui.size())

#define a .25ms pause after all steps
pyautogui.PAUSE = .25

#load up workstation.exe
pyautogui.hotkey('win')
pyautogui.write('workstation')
pyautogui.hotkey('enter')

#move to middle of screen and click to select window
pyautogui.moveTo(size[0]/2,size[1]/2)
pyautogui.click()

#get to application screen
pyautogui.hotkey('enter')
pyautogui.hotkey('1')
pyautogui.hotkey('enter')
pyautogui.write(userName)
pyautogui.hotkey('enter')
pyautogui.write(passWord)
pyautogui.hotkey('enter')

#get to MM item edit
pyautogui.hotkey('pgdn')
pyautogui.hotkey('1')
pyautogui.hotkey('enter')

#90->70->14
pyautogui.write('90')
pyautogui.hotkey('enter')
pyautogui.write('70')
pyautogui.hotkey('enter')
pyautogui.write('14')
pyautogui.hotkey('enter')

for item in items:
    pyautogui.PAUSE = .5
    pyautogui.write(item)
    pyautogui.hotkey('enter')
    pyautogui.hotkey('y')
    pyautogui.write('14')
    pyautogui.hotkey('enter')