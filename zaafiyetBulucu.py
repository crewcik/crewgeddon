import time
from colorama import Fore
import os 
import subprocess


def zaafiyet():

    ip = input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}IP / Domain: ")

    if not ip:
        print(f"{Fore.RED}[CREWGEDDON]: {Fore.WHITE}IP Adresi boş bırakılamaz.")
    
    
    kayit_edilsin_mi = input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}Veriler Kayıt Edilsin Mi? (e/h): ").lower()
    
    tarama = f"nmap -sS -sV -p- -T4 -A --script=vuln,default --open -Pn {ip}"
    if kayit_edilsin_mi == "e":
        tarama = f"nmap -sS -sV -p- -T4 -A --script=vuln,default --open -Pn {ip} -o {ip}_tarama"
    elif kayit_edilsin_mi == "h":
    	tarama = f"nmap -sS -sV -p- -T4 -A --script=vuln,default --open -Pn {ip}"
    else:
    	tarama = f"nmap -sS -sV -p- -T4 -A --script=vuln,default --open -Pn {ip}"
    
    print(f"{Fore.GREEN}[CREWGEDDON]: {Fore.WHITE}Zaafiyet taraması 2 saniye içerisinde başlatılacaktır.")
    time.sleep(2)
    subprocess.Popen([
        "xterm",
        "-T", f"CREWGEDDON - Zaafiyet Taraması ({ip})",
        "-hold",
        "-e", tarama
    ])
    time.sleep(1)
    print(f"{Fore.YELLOW}[Duyuru]: {Fore.WHITE}Tarama tam tarama olarak devam etmektedir ve zaafiyetleri bulması biraz zaman alabilir.")
    print(f"{Fore.YELLOW}[Duyuru]: {Fore.WHITE}Tarama bittikten sonra tarama pencesini kapatabilirsiniz.")
    print(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}Herhangi bir sonuç gelmez ise zaafiyet taramasını tekrar yapın.")
    time.sleep(20)
