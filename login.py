from password import *
import os
from colorama import Fore,init
init()
def ban():
    os.system('clear')
    os.system('figlet HACKER | lolcat')
    print("""
    
    """)
    os.system(Fore.YELLOW+'')
    os.system('date')

    print(Fore.WHITE+"")
    global cd
    cd = input('enter your passwd:')
ban()
    
while(1):
    try:
        if cd ==password:
            os.system('clear')
            os.system('cd')
            break
        else:
            print(Fore.RED+"password is wrong :|")
            print(Fore.WHITE+"")
            ban()
    except KeyboardInterrupt:
           print(Fore.RED+'TRy again ....')
           print(Fore.WHITE+"")

    
