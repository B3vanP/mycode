#!/usr/bin/env python3
"""Alta3 Research | Exploring interfaces library"""

import netifaces

def get_mac_address(interface):
    try:
        return (netifaces.ifaddresses(interface)[netifaces.AF_LINK])[0]['addr']
    except KeyError:
        return 'Could not collect MAC address'

def get_ip_address(interface):
    try:
        return (netifaces.ifaddresses(interface)[netifaces.AF_INET])[0]['addr']
    except KeyError:
        return 'Could not collect IP address'

def main():
    print(netifaces.interfaces())

    for i in netifaces.interfaces():
        print('\n****** details of interface - ' + i + ' ******')
        print('MAC: ', end='') # This print statement will always print MAC without an end of line
        print(get_mac_address(i)) # Prints the MAC address using the function
        print('IP: ', end='')  # This print statement will always print IP without an end of line
        print(get_ip_address(i)) # Prints the IP address using the function

if __name__ == "__main__":
    main()

