from colorama import Fore
import os
import time

def altAlanAdi():
    domain = input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}Domain'i belirtin (crewdev.com.tr): ").strip()
    print(f"{Fore.CYAN}[CREWGEDDON]: {Fore.WHITE}Arama başlatıldı...")

    os.system(f"subfinder -d {domain}")
    time.sleep(13)
    return domain
