import pyautogui
import time
import random
import threading
from colorama import Fore
import pyfiglet

class Valorant:
    def __init__(self):
        self.option = int(input(Fore.YELLOW + "Choose Your Option:\n\n1. AutoTyper/Spammer\n2. Anti-AFK Random Movement\n\n>>> " + Fore.RESET))
        
        if self.option == 1:
            self.MsgSpammer()
        elif self.option == 2:
            self.AutoMove()
        else:
            print(Fore.RED + "Invalid option. Please choose 1 or 2." + Fore.RESET)

    def MsgSpammer(self):
        """ Spams a user-defined message for a given amount of times with a delay. """
        w = input("> Msg to spam :: ")
        s = int(input("> Msg amount to spam :: "))
        a = float(input("> Msg spam time interval :: "))

        try:
            for x in range(s):
                pyautogui.typewrite(w)
                pyautogui.press('enter')
                time.sleep(a)
        except KeyboardInterrupt:
            print(Fore.RED + "\n>> Task Interrupted Due To Keyboard Interruption.." + Fore.RESET)

    def AutoMove(self):
        """ Simulates random movements to prevent being flagged as AFK. """
        move_keys = input("> Enter movement keys (default: wasd) :: ") or "wasd"
        duration = int(input("> Run time in seconds (0 for infinite) :: "))

        start_time = time.time()
        print(Fore.GREEN + "# AutoMove Started " + Fore.RESET)

        try:
            while duration == 0 or time.time() - start_time < duration:
                movement = random.choice(move_keys)
                weapon_switch = random.choice([True, False])
                
                pyautogui.keyDown(movement)
                time.sleep(random.uniform(0.15, 0.3))
                pyautogui.keyUp(movement)
                
                if weapon_switch:
                    pyautogui.press(random.choice(['2', '3', 'E']))
                
                if random.randint(1, 5) == 3:
                    pyautogui.press('space')
                
                if random.randint(1, 7) == 2:
                    pyautogui.keyDown('ctrl')
                    time.sleep(random.uniform(0.2, 0.5))
                    pyautogui.keyUp('ctrl')

                pyautogui.moveRel(random.randint(-50, 50), random.randint(-50, 50), duration=0.2)

                time.sleep(0.5)

        except KeyboardInterrupt:
            print(Fore.RED + "\n>> Task Interrupted Due To Keyboard Interruption.." + Fore.RESET)

if __name__ == "__main__":
    title = pyfiglet.figlet_format("Anti-AFK")
    print(Fore.MAGENTA + title)
    Valorant()
