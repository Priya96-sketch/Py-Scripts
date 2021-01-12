---
# PROJECT - Find IP Address of any Website and your PCs as well
#Author : Priya Mondal
---

#IP Addresses helps in connecting our computer to other devices on the Network & all over the world
#IP-> Internet Protocol Address
#For more information,visit Wikipedia

import socket as s

#Fetch a Host Name
my_hostname = s.gethostname()

#display
print('Your host name is: ' + my_hostname)

#Fetch the IP Address
my_ip = s.gethostbyname(my_hostname)
print('Your IP Address is: ' + my_ip)

host = 'freecodecamp.org'

ip = s.gethostbyname(host)

print('IP Address: ' + ip)
