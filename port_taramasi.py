from colorama import Fore
import subprocess
import time

def portTaramasi():
      ip = input(f'{Fore.GREEN}[CREWGEDDON]: {Fore.WHITE}IP Adresi: ')
      if not ip:
            print(f"{Fore.RED}[CREWGEDDON]: {Fore.WHITE}Lütfen IP adresini boş bırakmayınız.")
            return ip
      
      print(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}Port taraması başlatılıyor, IP: {ip}")
      time.sleep(2)
      subprocess.Popen([
            "xterm",
            "-T", "CREWGEDDON - Gelişmiş Port Taraması",
            "-hold",
            "-e",
            f"rustscan -a {ip}"
      ])