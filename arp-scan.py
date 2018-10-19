#!/usr/bin/env python

#Importing the logging module
import logging

#This will suppress all messages that have a lower level of seriousness than error messages.
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
logging.getLogger("scapy.interactive").setLevel(logging.ERROR)
logging.getLogger("scapy.loading").setLevel(logging.ERROR)

#Importing Scapy and handling the ImportError exception
try:
    from scapy.all import

except ImportError:
    print "Scapy package for Python is not installed on your system."
    print "Get it from https://pypi.python.org/pypi/scapy and try again."
    sys.exit()

#Performing the ping - discovering hosts on a local Ethernet network
#ans, unans = srp(Ether(dst = "ff:ff:ff:ff:ff:ff") / ARP(pdst = "172.16.1.0/24"), timeout = 5, iface = "enp0s3")

#ans.summary(lambda (s,r): r.sprintf("%Ether.src% %ARP.psrc%") )

#Using the builtin function
x = arping("10.10.10.*")
print "==========="
#
# y = x[0].show()
# print "+++++++++"
# print type(y)
# # print x[0][2]
# print type(x[0])
result_array = []
for snd, rcv in x[0]:
    mac_ip = rcv.sprintf(r"%Ether.src%,%ARP.psrc%")
    ip = mac_ip.split(',')[1]
    result_array.append(ip)

print result_array