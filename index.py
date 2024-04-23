import pyautogui
import time
import random
from colorama import Fore
import pyfiglet

class Valorant:
    def __init__(self):
        self.option = int(input(Fore.YELLOW +"Choose Your Option:\n\n1. AutoTyper/Spammer\n2. Anti-AFK Random Movement\n\n>>> "+ Fore.RESET))
        if self.option == 1:
            self.MsgSpammer()
        elif self.option == 2:
            self.AutoMove()
        else:
            print(Fore.RED +"Invalid option. Please choose 1 or 2."+ Fore.RESET)

    def MsgSpammer(self):
        w = input("> Msg to spam:: ")
        s = int(input("> Msg amount to spam :: "))
        a = float(input("> Msg spam time interval :: "))
        try:
            for x in range(s):
                pyautogui.typewrite(w)
                pyautogui.press('enter')
                time.sleep(a)
        except KeyboardInterrupt:
            print(Fore.RED +"\n>> Task Interrupted Due To Keyboard Interruption.."+ Fore.RESET)

    def AutoMove(self):
        print(Fore.GREEN + "# AutoMove Started " + Fore.RESET)
        try:
            while True:
                Movement = random.choice(['w', 's', 'a', 'd'])
                WeaponSwitch = random.choice([True, False])
                
                if Movement == 'w':
                    pyautogui.keyDown('w')
                    time.sleep(0.2)
                    pyautogui.keyUp('w')
                elif Movement == 's':
                    pyautogui.keyDown('s')
                    time.sleep(0.2)
                    pyautogui.keyUp('s')
                elif Movement == 'a':
                    pyautogui.keyDown('a')
                    time.sleep(0.2)
                    pyautogui.keyUp('a')
                elif Movement == 'd':
                    pyautogui.keyDown('d')
                    time.sleep(0.2)
                    pyautogui.keyUp('d')
                    
                if WeaponSwitch:
                    pyautogui.press(random.choice(['2', '3', 'E']))
                time.sleep(0.5)
        except KeyboardInterrupt:
            print(Fore.RED +"\n>> Task Interrupted Due To Keyboard Interruption.."+ Fore.RESET)

if __name__ == "__main__":
    title = pyfiglet.figlet_format(f"Anti-AFK")
    print(Fore.MAGENTA+title)
    Valorant()
