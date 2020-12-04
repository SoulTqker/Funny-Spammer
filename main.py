import pyautogui, time

time.sleep(20)  ##  YOU CAN CHANGE THE TIME BEFORE SPAMMING HERE

f = open("Script.txt", "r")
for words in f:
    pyautogui.typewrite(words)
    pyautogui.press("enter")
