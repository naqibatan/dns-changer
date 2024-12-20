import subprocess
import os
import ctypes
import tkinter as tk
from tkinter import messagebox

def is_admin():
    """
    Check if the script is running with administrative privileges.
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def change_dns(network_name, ipv4_dns, ipv6_dns):
    try:
        # Set IPv4 DNS
        subprocess.run(
            ["netsh", "interface", "ipv4", "set", "dnsservers", network_name, "static", ipv4_dns, "primary"],
            check=True
        )

        # Set IPv6 DNS
        subprocess.run(
            ["netsh", "interface", "ipv6", "set", "dnsservers", network_name, "static", ipv6_dns, "primary"],
            check=True
        )

        return True
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while setting DNS: {e}")
        return False

def get_network_details():
    details = {}

    # Get hostname
    details['Hostname'] = subprocess.getoutput("hostname")

    # Get MAC address
    details['MAC Address'] = subprocess.getoutput("getmac /v /fo list | findstr Physical")

    # Get IPv4 Address
    details['IPv4 Address'] = subprocess.getoutput("ipconfig | findstr IPv4")

    # Get IPv4 DNS
    details['IPv4 DNS'] = subprocess.getoutput("nslookup | findstr Address")

    # Get IPv6 Address
    details['IPv6 Address'] = subprocess.getoutput("ipconfig | findstr IPv6")

    # Get IPv6 DNS
    details['IPv6 DNS'] = subprocess.getoutput("ipconfig /all | findstr 'DNS Servers'")

    return details

def on_change_dns():
    IPV4_DNS = "[Your IPv4 DNS]"
    IPV6_DNS = "[Your IPv6 DNS]"
    network_name = "Ethernet"  # Change this to match your adapter name

    if change_dns(network_name, IPV4_DNS, IPV6_DNS):
        details = get_network_details()
        result = (f"Your DNS server has been changed!\n\n"
                  f"Below are your current network details:\n\n"
                  f"Hostname: {details['Hostname']}\n"
                  f"MAC Address: {details['MAC Address']}\n"
                  f"IPv4 Address: {details['IPv4 Address']}\n"
                  f"IPv4 DNS: {details['IPv4 DNS']}\n"
                  f"IPv6 Address: {details['IPv6 Address']}\n"
                  f"IPv6 DNS: {details['IPv6 DNS']}\n")

        messagebox.showinfo("DNS Changed", result)
    else:
        messagebox.showerror("Error", "Failed to change DNS settings. Please try again.")

def main():
    if not is_admin():
        messagebox.showerror("Permission Error", "Please run this script as an administrator.")
        return

    # Create the main window
    root = tk.Tk()
    root.title("DNS Changer")
    root.geometry("400x200")

    label = tk.Label(root, text="Click the button below to change DNS settings.", font=("Arial", 12))
    label.pack(pady=20)

    change_button = tk.Button(root, text="Change DNS", font=("Arial", 12), command=on_change_dns)
    change_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
