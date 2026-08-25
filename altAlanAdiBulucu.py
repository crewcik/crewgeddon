from colorama import Fore
import requests
import time

def altAlanAdi():
    domain = input(f"{Fore.BLUE}[CREWGEDDON]: {Fore.WHITE}Domain'i belirtin (crewdev.com.tr): ").strip()
    
    url = f"https://crt.sh/?q=%25.{domain}&output=json"

    print(f"{Fore.CYAN}[CREWGEDDON]: {Fore.WHITE}Arama başlatıldı...")

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    data = None

    for i in range(3):
        try:
            resp = requests.get(url, headers=headers, timeout=20)

            if resp.status_code != 200:
                print(f"{Fore.YELLOW}[CREWGEDDON]: {Fore.WHITE}Deneme {i+1} başarısız (Status: {resp.status_code})")
                time.sleep(2)
                continue

            data = resp.json()
            break

        except requests.RequestException:
            print(f"{Fore.YELLOW}[CREWGEDDON]: {Fore.WHITE}Deneme {i+1} başarısız, tekrar deneniyor...")
            time.sleep(2)

        except ValueError:
            print(f"{Fore.RED}[CREWGEDDON]: {Fore.WHITE}JSON parse hatası.")
            return

    if not data:
        print(f"{Fore.RED}[CREWGEDDON]: {Fore.WHITE}Veri alınamadı.")
        return

    subs = set()

    for entry in data:
        name = entry.get("name_value")
        if not name:
            continue

        for n in name.splitlines():
            n = n.strip()

            # wildcard temizleme
            if n.startswith("*."):
                n = n[2:]

            if n.endswith(domain):
                subs.add(n)

    if not subs:
        print(f"{Fore.RED}[CREWGEDDON]: {Fore.WHITE}Subdomain bulunamadı.")
        return

    print(f"\n{Fore.GREEN}[CREWGEDDON]: {Fore.WHITE}Bulunan subdomainler:\n")

    for sub in sorted(subs):
        print(f"{Fore.CYAN}➜ {sub}")