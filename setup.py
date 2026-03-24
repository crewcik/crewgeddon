import os

os.system("python3 -m venv crewgeddon")
os.system("bash -c 'source crewgeddon/bin/activate && pip install colorama pymysql requests && python crew.py'")
