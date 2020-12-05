import pyautogui, time
print("Welcome to the Script Spammer, do you want to use it ? Y/N")
answ = input("")

if answ in ["Yes", "yes", "Y", "y"]:
    start()
if answ in ["No", "no", "N", "n"]:
    print("Ok, ending the program...")
    pass
def start(time):
    print(f"You have now {time} seconds to open the tchat box where you want to  spam")
    time.sleep(time)

    f = open("Script.txt", "r")
    for words in f:
        pyautogui.typewrite(words)
        pyautogui.press("enter")
