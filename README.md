# dns-changer
Changing DNS Server in Windows 10 and Windows 11 with using Python


# How to start?

1. update the Your IPv4 DNS address and IPv6 DNS address in dns-change.py.
2. Change the network adapter in dns-change.py according to your preference. in dns-change.py, at network_name, Change 'Wifi' for wireless connection, Change 'Ethernet' for wired connection.
3. after making the changes, run this script 'pyinstaller --onefile --noconsole --manifest=dns-change.manifest dns-change.py' to ensure the file is build in windows.exe

 
