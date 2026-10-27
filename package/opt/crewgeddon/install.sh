#!/bin/bash

echo "[CREWGEDDON] kuruluyor..."

sudo mkdir -p /opt/crewgeddon

sudo wget -O /opt/crewgeddon/setup.py https://raw.githubusercontent.com/crewcik/crewgeddon/main/setup.py

sudo chmod +x /opt/crewgeddon/setup.py

echo '#!/bin/bash
python3 /opt/crewgeddon/setup.py "$@"' | sudo tee /usr/local/bin/crewgeddon > /dev/null

sudo chmod +x /usr/local/bin/crewgeddon

echo "[CREWGEDDON] hazır. crewgeddon yaz çalıştır."