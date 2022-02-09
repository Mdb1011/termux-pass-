import requests
from password import *
import os
from colorama import init,Fore
import time
init()
def baner():
    os.system("clear")

    print(Fore.WHITE+'              ______________________________________  ')      
    print(Fore.CYAN+'     ________|                                      |_______ ')
    print(Fore.CYAN+'     \       |      WELCOME TO THE termux-pass      |      / ')
    print(Fore.CYAN+'      \      |        Coded by Mohammad Tork        |     /  ')
    print(Fore.CYAN+'      /      |______________________________________|     \  ')
    print(Fore.CYAN+'     (__________)                                (_________) ')
    print("")
    print(Fore.RED+"[1]"+Fore.WHITE+" change password")
    print(Fore.RED+"[2]"+Fore.WHITE+" Check my ip")
    print(Fore.RED+"[3]"+Fore.WHITE+" passwd Genrator")
    print(Fore.RED+"[4]"+Fore.WHITE+" about me")
    print(Fore.WHITE+"")
                                        
baner()                    
raw = input("[+]-->To continue select one :")                    
                                        



def pas():
                    try:
                        s = input("Enter your password:")
                        filename = "password.py"
                        file = open(filename, "w")
                        file.write("'++++++++++++++++++++++++++++++++++++++++++++++'\n"+'password = "'+s+'"'+"\n'**********************************************'")
                        file.close()
                        print("\033[36m[*] old your password : "+password)
                        print("\033[33m[*] new your password : "+s)
                        print('\033[32m[+] YOUR PASSWORD CHANGED :)')
                        print(Fore.WHITE+"")
                    except:
                        pas()
if raw =='1':
    os.system('clear')
    pas()

if raw =='2':
                    try:   
                       
                        print("")
                        css = requests.get('https://api.myip.com')
                        ip = css.json()['ip']
                        contry = css.json()['country']
                        cc = css.json()['cc']
                        os.system('figlet check-ip | lolcat')
                        print("""
                                        
                        """)
                        print(Fore.GREEN+'[=] country :'+Fore.WHITE+ contry)
                        print(Fore.GREEN+'[=] cc      :'+Fore.WHITE+ cc)
                        print(Fore.GREEN+'[=] ip      :'+Fore.WHITE+ ip )
                        print("")

                        
                    except:
                            print(Fore.RED+"ERROR")

if raw =='4':
    try:
        print("")
        os.system('cls')
        print("")
        print(Fore.RED+'</>'+Fore.GREEN+' Im Mohammad coder ,a programmer fluent in python :)')
        print("")
        print(Fore.RED+"</> "+Fore.BLUE+"Telegram : "+Fore.YELLOW+'Mohammad_tork_apk')
        print("")
        print(Fore.RED+'</>'+Fore.BLUE+' Rubika   : '+Fore.YELLOW+'mamal_fi')
        print("")
        print(Fore.RED+'</> '+Fore.BLUE+'whatsapp : '+Fore.YELLOW+'+1248764-5338')
        print(Fore.WHITE+"")
    except:
        print(Fore.RED+"ERROR")

if raw =='3':
                    try:
                        print("")
                        os.system('clear')
                        os.system('figlet Passwd | lolcat')
                        pac = input("ENTER THE NUMBER OF characters (defalt=10):")
                        cs = requests.get('https://api.codebazan.ir/password/?length='+pac).text
                        print("\033[32mpassword :" +cs)

                    except:
                            print(Fore.RED+"ERROR")






                    
                    




