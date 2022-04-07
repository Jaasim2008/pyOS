import colorama
from colorama import Fore
import os
import handler
import time
import webbrowser

colorama.init(autoreset=True)

print(f"{Fore.YELLOW}Welcome to PyOS [1.0]")
print("")
print(f"{Fore.RED}Press ENTER to Start")
input()
os.system("cls")
print(f"{Fore.GREEN} 'e' -> Exit, 'help' -> Help Page")


def starting():
    user_input_no_change = input("> ")
    user_input = user_input_no_change.lower()
    if user_input == "":
        starting()
    elif user_input == 1 or user_input == "1" or user_input == "calculator":
        cal = handler.os_apps_calculator()
        if cal == 0:
            starting()
        else:
            print(f"{Fore.RED}Unknown Error Occurred!")
    elif user_input == 2 or user_input == "2" or user_input == "weather" or user_input == "weather stats":
        weather_app = handler.os_apps_weather()
        if weather_app == 0:
            os.system("cls")
            starting()
        else:
            print(f"{Fore.RED}Unknown Error Occurred!")
    elif user_input == "help":
        webbrowser.open("https://github.com/Jaasim2008/pyOS/blob/main/README.md")
        os.system("cls")
        starting()
    elif user_input == "mk-file":
        if handler.os_mk_file() == 0:
            os.system("cls")
            starting()
        else:
            print(f"{Fore.RED}Unknown Error Occurred!")
    elif user_input == "mk-dir" or user_input == "mk-folder":
        if handler.os_mk_dir() == 0:
            os.system("cls")
            starting()
        else:
            print(f"{Fore.RED}Unknown Error Occurred!")
    elif user_input == "edit":
        if handler.os_text_editor() == 0:
            starting()
        else:
            print(f"{Fore.RED}Unknown Error Occurred!")
    elif user_input == "e":
        quit()
    else:
        print(f"{Fore.RED}Unknown Command!")

        time.sleep(0.5)

        os.system("cls")
        starting()


starting()
