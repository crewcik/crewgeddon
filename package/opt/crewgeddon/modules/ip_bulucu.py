from colorama import Fore
import time
import socket

def ipBulucu():
      url = input(f"{Fore.GREEN}[CREWGEDDON]: {Fore.WHITE}Domaini belirtin (crewdev.com.tr): ")
      
      if not url:
            print(f"{Fore.RED}[CREWGEDDON]: {Fore.WHITE}DOMAIN Boş bırakılamaz.")
            return url
      
      print(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}IP Gösteriliyor..")
      time.sleep(2)      
      ip_address = socket.gethostbyname(url)
      if ip_address:
            print(f"{Fore.GREEN}[CREWGEDDON]: {Fore.WHITE}{url} Sitesi'nin IP Adresi: {ip_address}")
            while True:
                  copySorusu = input(f"{Fore.CYAN}[CREWGEDDON]: {Fore.WHITE}Kopyaladınız mı? (e/h): ").lower()
                  if copySorusu == "e":
                        return ip_address
                  elif copySorusu == "h":
                        continue
                  else:
                        continue
      else:
            print(f"{Fore.RED}[CREWGEDDON]: {Fore.WHITE}Bu site şuan aktif değil.")