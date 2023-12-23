import numpy as nm

import pyautogui

import time

import sys

import time

import mouse

import keyboard

import  pytesseract

import cv2

from PIL import ImageGrab

from PIL import Image

def checkCorrect():
    x = False
    pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
    cap = ImageGrab.grab(bbox=(1591, 1089, 1620, 1109))
    now = time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())
    cap.save(now+".jpg")
    tesstr = pytesseract.image_to_string(
    cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY), lang = 'eng')
    print(tesstr)
    if(tesstr!="89"):
            keyboard.press('esc')
            keyboard.release('esc')
            time.sleep(1/10)
            keyboard.press('esc')
            keyboard.release('esc')
            time.sleep(1/10)
            mouse.move(1167, 805)
            time.sleep(1/10)
            mouse.click('left')
            print()
            time.sleep(1/10)
            while pyautogui.pixel(131, 1399)[0] != 123:
                mouse.move(131, 1399)
                mouse.click('left')
                x = True
    if x == True:
        all()
        sys.exit()
    

def canStart():
    while pyautogui.pixel(1595, 1102)[0] == 0:
        x = 0

def checkPassword():
    while pyautogui.pixel(1167, 1322)[0] != 22:
        x=1

def checkManager():
    while pyautogui.pixel(1585, 1000)[0] != 139:
        x=1

def checkManager2():
    while pyautogui.pixel(534, 754)[0] == 6:
        x=1

def id(floor, oned, d):
    x = False
    pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
    if d == True:
        cap = ImageGrab.grab(bbox=(402, 1086, 486, 1125))
    else:
        cap = ImageGrab.grab(bbox=(402, 1055, 482, 1087))

    now = time.strftime('%Y-%b-%d__%H_%M_%S',time.localtime())
    cap.save(now+".jpg")
    tesstr = pytesseract.image_to_string(
    cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY), lang = 'eng')

    for x in tesstr:
        tesstr = tesstr.replace("\n", "")
        tesstr = tesstr.replace("|", "J")
        tesstr = tesstr.replace("1", "I")
        tesstr = tesstr.replace("2", "Z")
        tesstr = tesstr.replace(")", "J")
        tesstr = tesstr.replace("]", "J")
        tesstr = tesstr.replace("}", "J")

    print("floor" + floor + "." + tesstr.upper() + "." + oned)

    if len(tesstr) != 3:
        print(len(tesstr))
        if tesstr == "":
            while pyautogui.pixel(131, 1399)[0] != 123:
                mouse.move(131, 1399)
                mouse.click('left')
                x = True                
        else:
            keyboard.press('esc')
            keyboard.release('esc')
            time.sleep(1/10)
            keyboard.press('esc')
            keyboard.release('esc')
            time.sleep(1/10)
            mouse.move(1167, 805)
            time.sleep(1/10)
            mouse.click('left')
            print()
            time.sleep(1/10)
            while pyautogui.pixel(131, 1399)[0] != 123:
                mouse.move(131, 1399)
                mouse.click('left')
                x = True

    if x == True:
        all()
        sys.exit()

    keyboard.write("floor" + floor + "." + tesstr.upper() + "." + oned)
    time.sleep(1/10)
    keyboard.press('enter')
    keyboard.release('enter')

def all():
    mouse.move(1293, 802)
    time.sleep(5/10)
    mouse.click('left')
    time.sleep(20/10)
    canStart()

    mouse.move(1980, 1140)
    mouse.click('left')
    time.sleep(60/10)
    mouse.move(2250, 830)
    mouse.click('left')
    time.sleep(1)
    mouse.move(560, 960)
    mouse.click('left')
    checkPassword()
    keyboard.write('HPFNA')
    keyboard.press('enter')
    keyboard.release('enter')
    checkManager()
    keyboard.write('run powermanager')
    keyboard.press('enter')
    keyboard.release('enter')
    time.sleep(1/10)
    keyboard.press('esc')
    keyboard.release('esc')
    mouse.move(1167,1322)
    time.sleep(60/10)
    mouse.move(1167,1022)
    time.sleep(1/10)
    mouse.move(1167,1322)
    time.sleep(1/10)
    mouse.move(976, 947)
    mouse.click('left')
    time.sleep(1/10)
    mouse.move(840, 830)
    mouse.click('left')
    time.sleep(1/10)
    mouse.move(2000, 1370)
    mouse.click('left')
    time.sleep(1/10)
    checkManager2()
    time.sleep(1/10)
    keyboard.press('enter')
    keyboard.release('enter')
    mouse.move(987, 635)
    time.sleep(1/10)
    id("E", "off", False)
    mouse.move(815, 534)
    for x in range(8):
        mouse.wheel(1)
    time.sleep(1/10)
    id("C", "off", True)
    mouse.move(788, 612)
    time.sleep(1/10)
    id("C", "off", True)
    mouse.move(821, 729)
    time.sleep(1/10)
    id("C", "on", False)
    time.sleep(1/10)
    mouse.wheel(1)
    mouse.wheel(1)
    mouse.wheel(1)
    mouse.wheel(1)
    mouse.move(468, 905)
    time.sleep(1/10)
    id("B", "on", False)
    mouse.move(822, 786)
    time.sleep(1/10)
    id("B", "on", False)
    mouse.move(468, 306)
    time.sleep(1/10)
    id("A", "on", False)
    time.sleep(1/10)
    keyboard.press('esc')
    keyboard.release('esc')
    time.sleep(1/10)
    mouse.move(1280, 720)
    time.sleep(1/10)
    mouse.click('left')
    time.sleep(1/10)
    keyboard.wait('space')
    all()
    sys.exit()

keyboard.wait('space')
all()
sys.exit()