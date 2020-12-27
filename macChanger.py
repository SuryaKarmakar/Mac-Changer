import subprocess

def mac_Changer(interface, newMac):
    subprocess.call(["ifconfig",interface])
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",newMac])
    subprocess.call(["ifconfig",interface,"up"])
    subprocess.call(["ifconfig",interface])

def main():
    interface = input("[+]Enter your interface name : ")
    newMac = input("[+]Enter your new mac address : ")
    mac_Changer(interface, newMac)
if __name__ == "__main__":
    main()