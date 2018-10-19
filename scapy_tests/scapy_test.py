from scapy.all import *

# traceroute('www.google.com', maxttl=10)
ans = sr1(IP(dst="192.168.8.102") / ICMP(), verbose=0, timeout=5)
# print ans.__getitem__(0)
# print ans.filter('ICMP')
# print help(ans.show())
ans.show()
print len(ans)
# print unans
# print sr.__doc__
