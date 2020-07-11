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
* Visit https://[IP Address of the Raspberry Pi in IFL-Intranet]:10000/ to open the Webmin Web-GUI

## Directory
* Website: /var/www/html/
* Python-Script: /home/pi/blackhole.py

## Auto-Restart after Reboot (Done)

### Python-Script
* Add "sudo python /home/pi/blackhole.py &" before "exit 0" of /etc/rc.local (Done)
* Make sure the rc-local.service is running, use "systemctl enable rc-local.service" to enable it (Done)
* Then the Python-Script for Taking Photos every 5 seconds will run automatically when the Raspberry Pi reboots

### Apache Server
* Done with the same way

***

## Done List
* Front-End Page created and tested
* Raspberry Pi OS updated (SD Card reburned with the newest offical Image) in order to fix Camera Issues
* Webmin, Apache and other necessary software installed
* Auto-Restart Script for Apache Server and Python-Script deployed and tested
* Reachability and Functionality of the System in Home-LAN tested

## To-Do List
* Link the Raspberry Pi into IFL-Intranet
* Set its Domain Name to http://blackhole.ifl.kit.edu within the IFL-internal DNS System
* Modify Apache Web-Server Configuration, set the Address of this virtuell Server to http://blackhole.ifl.kit.edu
* Test the Reachability and Functionality of the System
