# Bu TOOLS Tamamen eğitim amaçlı kodlanmıştır, kötüye kullanırsanız ilk ben bulurum. <3☺️

from colorama import Fore
import os
import time

import port_taramasi
import ip_bulucu
import ddos_sistem
import mainText
import mySql
import altAlanAdiBulucu
import trojen_sistem
import keyLogger_sistem
import wifi_hack

import subprocess

interface = "wlan0"  # Monitör modundan sonra sonuna "wlan0mon" eki gelebilir, burayı oraya göre düzeltin, adını iwconfig yazıp öğrenebilirsiniz.

os.system("clear")
mainText.mainText()

while True:
    try:
        select = input(f"{Fore.CYAN}CREWGEDDON~#: {Fore.WHITE}")

        if select == "1":
            port_taramasi.portTaramasi()
            mainText.mainText()

        elif select == "2":
            ip_bulucu.ipBulucu()
            mainText.mainText()

        elif select == "3":
            ddos_sistem.ddosSystem()
            mainText.mainText()

        elif select == "4":
            mySql.mySql()
            mainText.mainText()

        elif select == "5":
            altAlanAdiBulucu.altAlanAdi()
            mainText.mainText()

        elif select == "6":
            trojen_sistem.trojenSistem()
            mainText.mainText()

        elif select == "7":
            keyLogger_sistem.keyLoggerSistem()
            mainText.mainText()

        elif select == "8":
            wifi_hack.wifiHack(interface)
            mainText.mainText()

        elif select == "9":
            os.system(f"airmon-ng start {interface}")
            print(f"{Fore.GREEN}[CREWGEDDON]: {Fore.WHITE}Başarıyla monitör moda geçiş yapıldı.")
            time.sleep(2)
            mainText.mainText()

        elif select == "10":
            os.system(f"airmon-ng stop {interface}")
            print(f"{Fore.GREEN}[CREWGEDDON]: {Fore.WHITE}Başarıyla managed moda geçiş yapıldı.")
            time.sleep(2)
            mainText.mainText()

        elif select == "11":
            print(f"{Fore.YELLOW}[CREWGEDDON]: {Fore.WHITE}Crewgeddon kapatıldı, tekrardan görüşmek üzere...")
            time.sleep(2)
            os.system("exit")
            os.system("clear")
            break

        else:
            print(f"{Fore.RED}[CREWGEDDON]: {Fore.WHITE}Geçersiz seçim yaptınız.")
    except KeyboardInterrupt:
        while True:
            try:
                cikis = input(f"\n{Fore.CYAN}[CREWGEDDON]: {Fore.BLUE}Kapatmak istediğinize emin misiniz? (e/h) ").lower()
            except KeyboardInterrupt:
                print(f"{Fore.CYAN}\n[CREWGEDDON]: {Fore.BLUE}Crewgeddon zorla kapatıldı.")
    
            if cikis == "e":
                quit()
            elif cikis == "h":
                mainText.mainText()
                os.system("python3 crew.py")
            else:
                continue