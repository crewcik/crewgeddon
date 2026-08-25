import os
from colorama import Fore
import subprocess
import time


def yerelAgSaldirisi(interface):
    bit = 16
    
    print(f"{Fore.YELLOW}[1] - {Fore.GREEN}eth0 (Local Ağ) {Fore.YELLOW}[2] - {Fore.GREEN}{interface}")
    wifi_secim = int(input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}Seçim: "))
    interface_secim = interface
    if wifi_secim == 1:
        interface_secim = "eth0"
    elif wifi_secim == 2:
        interface_secim = interface
    else:
        interface_secim = "eth0"
    os.system('ifconfig')
    ip = input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}{interface_secim} inet IP: ")
    bit_secim = int(input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}Bit (8,16, 24 - default = {bit}): "))
    	
    if bit_secim == 8:
        bit = 8
    elif bit_secim == 16:
        bit = 16
    elif bit_secim == 24:
        bit = 24
    else:
        bit = 16
        
    subprocess.Popen([ "xterm", "-T", "Crewgeddon - Yerel Ağ İzleyicisi", "-hold", "-e", f"netdiscover -i {interface_secim} -r {ip}/{bit}",])
    time.sleep(10)
    print(f"{Fore.YELLOW}[Duyuru]: {Fore.WHITE}Yerel ağ izlencisini istediğiniz zaman kapatabilirsiniz.")
    time.sleep(20)
