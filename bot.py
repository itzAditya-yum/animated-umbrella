import pyautogui
import time

text = open('dumb.txt', 'r')
time.sleep(5)

for word in text:
    pyautogui.typewrite(word)
    pyautogui.press('enter')
    time.sleep(2)