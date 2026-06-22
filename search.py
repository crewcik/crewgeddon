from colorama import Fore
import time
import subprocess
import os
import requests

def altAlanAdi():
      domain = input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}Domain'i belirtin (crewdev.com.tr): ").strip()
      url = f"https://crt.sh/?q=%25.{domain}&output=json"

      try:
        resp = requests.get(url, timeout=30)
        resp.raise_for_status()
      except requests.RequestException as e:
         print(f"{Fore.RED}[CREWGEDDON]: {Fore.WHITE}Bir sorun oluştu, lütfen tekrar deneyin.")
      try:
         data = resp.json()
      except ValueError:
         print(f"{Fore.RED}[CREWGEDDON]: {Fore.WHITE}Bir sorun oluştu, lütfen tekrar deneyin.")
      subs = set()
      
      for entry in data:
            name = entry.get("name_value")
            if not name:
                continue
            for n in name.splitlines():
                n = n.strip()
                if n.endswith(domain):
                    subs.add(n)

      if not subs:
            print(f"{Fore.RED}[CREWGEDDON]: {Fore.WHITE}Alt alan adları bulunamadı.")
      else:
            for sub in sorted(subs):
                  subprocess.Popen([
                        "xterm",
                        "-T", f"CREWGEDDON - ({domain}) Alt Alan Adları Bulucu",
                        "-hold",
                        "-e",
                        f"{Fore.CYAN}[CREWGEDDON]: {Fore.WHITE}{sub}"
                  ])

altAlanAdi()
