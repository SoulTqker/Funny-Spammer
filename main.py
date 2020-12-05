import pyautogui
from time import sleep
print("Welcome to the Script Spammer, do you want to use it ? Y/N")
answ = input("")
time = input("How much time do you need before clicking in the tchat box ? :")

def start(time):
    print(f"You have now {time} seconds to open the tchat box where you want to  spam")
    sleep(int(time))

    f = open("Script.txt", "r")
    for words in f:
        pyautogui.typewrite(words)
        pyautogui.press("enter")


if answ in ["Yes", "yes", "Y", "y"]:
    start(time)
if answ in ["No", "no", "N", "n"]:
    print("Ok, ending the program...")
    pass
