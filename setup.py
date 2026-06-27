import os
import time

os.system("apt install figlet")
os.system("figlet crewgeddon setup installer")
time.sleep(2)
os.system("python3 -m venv crewgeddon")
os.system("bash -c 'source crewgeddon/bin/activate && pip install colorama pymysql requests && python crew.py'")
