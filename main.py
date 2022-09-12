import os
import time
import sys
try:
    from colorama import Fore, Style
except ModuleNotFoundError:
    os.system("py -m pip install colorama")
    from colorama import Fore, Style
try:
    import configparser
except ModuleNotFoundError:
    os.system("py -m pip install configparser")
    import configparser

VERSION = "FREE" # PAID OR FREE
config = configparser.ConfigParser()
config.read("config.ini")
type = config['CONFIG']['type']	

def path(relative):
    return os.path.join(
        os.environ.get(
            "_MEIPASS2",
            os.path.abspath(".")
        ),
        relative
    )

if type == "LOCK":
    pass
elif type == "SHUTDOWN":
    pass
elif type == "BLUESCREEN":
    pass
else:
    print("INVALID CONFIG FILE.")
    time.sleep(5)
    sys.exit

if VERSION == "FREE":
    os.system("start credits.txt")
else:
    pass


os.system('wscript.exe "hide.vbs" "sound.bat"')
print("Shutting Down in: 15")
# time.sleep(1)
print("Shutting Down in: 14")
time.sleep(1.25)
print("Shutting Down in: 13")
time.sleep(1.25)
# print("Shutting Down in: 14")
# time.sleep(1)
# print("Shutting Down in: 13")
# time.sleep(1)
print("Shutting Down in: 12")
time.sleep(1.2)
print("Shutting Down in: 11")
time.sleep(1.2)
print("Shutting Down in: 10")
time.sleep(1.2)
print("Shutting Down in: 9")
time.sleep(1.2)
print("Shutting Down in: 8")
time.sleep(1.2)
print("Shutting Down in: 7")
time.sleep(1.2)
print("Shutting Down in: 6")
time.sleep(1.2)
print(f"Shutting Down in: {Fore.RED}5{Style.RESET_ALL}")
time.sleep(1)
print(f"Shutting Down in: {Fore.RED}4{Style.RESET_ALL}")
time.sleep(1)
print(f"Shutting Down in: {Fore.RED}3{Style.RESET_ALL}")
time.sleep(1)
print(f"Shutting Down in: {Fore.RED}2{Style.RESET_ALL}")
time.sleep(1)
print(f"Shutting Down in: {Fore.RED}1{Style.RESET_ALL}")
time.sleep(1)

if type == "LOCK":
    os.system("Rundll32.exe user32.dll,LockWorkStation")
elif type == "SHUTDOWN":
    os.system("shutdown /p")
elif type == "BLUESCREEN":
    os.system("powershell wininit")
else:
    print("Something went wrong.")
    os.system("pause")

os.system('taskkill /fi "WINDOWTITLE eq OutroMusic-Identifier_8809431"')