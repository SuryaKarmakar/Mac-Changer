import subprocess
import optparse

#this function capture command line arguments
def get_Arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", metavar=" ", help="[+]Enter Interface to change it's MAC address, e.g : --interface eth0")
    parser.add_option("-m", "--mac", dest="newMac", metavar=" ", help="[+]Enter new MAC address, e.g : --mac aa:bb:cc:dd:ee:ff")
    (option, argument) = parser.parse_args()
    
    #checking user are specify a Interface and MAC or not
    if not option.interface:
        parser.error("[-]Please specify an Interface, use --help for more info...")
    elif not option.newMac:
        parser.error("[-]Please specify an new MAC, use --help for more info...")
    return option

#this function change your MAC address 
def mac_Changer(interface, newMac):
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",newMac])
    subprocess.call(["ifconfig",interface,"up"])
    subprocess.call(["ifconfig",interface])

def main():
    options = get_Arguments()
    mac_Changer(options.interface, options.newMac)
if __name__ == "__main__":
    main()
    