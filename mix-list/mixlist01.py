#!/usr/bin/env python3

# create a list containing three items
my_list = [ "192.168.0.5", 5060, "UP" ]

# display the first item in the list
print("The first item in the list (IP): " + my_list[0] )

# display the second item in the list
print("The second item in the list (port): " + str(my_list[1]) )

# display the third item in the list
print("The last item in the list (state): " + my_list[2] )

# display on the IP addresses from the iplist
iplist = [5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]

# Function to check if a string is a valid IP address
def is_ip_address(string):
    parts = string.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False
    return True

# Filter and display only IP addresses
for item in iplist:
    if isinstance(item, str) and is_ip_address(item):
        print(item)

