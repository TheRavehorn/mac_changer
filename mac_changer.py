#!/usr/bin/env python3
import subprocess


def greet():
    print("Linux MAC Changer 0.01 by Ravehorn!")


def show_info():
    print("Displaying info about your system devices:")
    subprocess.call(["sudo", "ifconfig"])


def change_mac(interface, mac):
    print("Changing MAC address for " + interface + " to " + mac)
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])


greet()
show_info()
my_interface = input("What interface do you want alter?\n")
new_mac = input("What MAC address do you desire?\n")
change_mac(my_interface, new_mac)
print("Program finished.")
