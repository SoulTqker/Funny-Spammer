import pyautogui, time

time.sleep(20)

f = open("Script.txt", "r")
for words in f:
    pyautogui.typewrite(words)
    pyautogui.press("enter")