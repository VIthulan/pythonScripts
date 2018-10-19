from scapy.all import *
import time
import math
import matplotlib.pyplot as plt

i = 10
index_arr = []
val_arr = []

while i < 64000:
    time1 = int(round(time.time() * 1000))
    packet = IP(dst="10.10.10.126") / ICMP() / Raw(RandString(size=i))

    send(packet)

    time2 = int(round(time.time() * 1000))

    time_taken = (time2 - time1)
    print "took  " + str(time_taken) + "ms"
    index_arr.append(i)
    val_arr.append((i / (time2 - time1)) / math.pow(10, 3))

    i = i + 100

plt.plot(index_arr, val_arr)
plt.legend(['Bandwidth'], loc='upper left')
plt.xlabel('Packets Size')
plt.show()
