# Blackhole-IFL
The Blackhole Observer of IFL based on Raspberry Pi 3B+ and Pi Camera Module.

## Hardware
* Raspberry Pi 3 Model B Rev 1.2 with 1GB RAM
* Raspberry Pi Camera Module (I) Rev 2.2

## Enviorment
* Raspberry Pi OS (32-bit) with desktop Ver 2020.05
* Webmin Ver 1.953
* Apache Ver 2.4.38 (Raspbian)

## Maintenance
* Use SSH-Client to do Maintenance manually
* Visit https://[IP Address of the Raspberry Pi in IFL-Intranet]:10000/ to open the Webmin Web-GUI in order to:
    1. Monitor Server Health
    2. Modify Apache Web-Server Configuration
    3. and many useful Funktions...
    
## Directory
* Website: /var/www/html/
* Python-Script: /home/pi/blackhole.py

## Auto-Restart for Python-Script
* Add "sudo python /xx/xx/xx.py" before "exit 0" of /etc/rc.local
* Make sure the rc-local.service is running, use "systemctl enable rc-local.service" to enable it
