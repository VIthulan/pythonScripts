import subprocess
# import matplotlib.pyplot as plt

print "Enter IP to find the latency and packet loss\n",
# IP_ADDRESS = raw_input()
IP_ADDRESS = '10.10.10.126'

NO_OF_TESTS = range(1, 3)


def get_latency(count=5, size=64):
    c = '-c%s' % count
    s = '-s%s' % size
    p = subprocess.Popen(["ping", c, s, IP_ADDRESS], stdout=subprocess.PIPE)
    res = p.communicate()[0].splitlines()
    # print res
    average_latency = res[-1].replace('rtt min/avg/max/mdev = ', '').replace(' ms', '').split('/')

    avg_packet_loss = res[-2].split(',')[2].rstrip().lstrip().replace(' packet loss', '').replace(
        '%', '')

    print 'Packet count: %s' % count
    print 'Packet Size: %s' % size
    print 'Average latency: %s ms' % average_latency[1]
    print 'Packet loss: %s%%' % avg_packet_loss

    return average_latency[1], avg_packet_loss


latency_data = []
packet_loss_data = []
packet_size = []

size_file = open("size_file.txt", "w+")
lat_file = open("lat_file.txt", "w+")
pack_file = open("pack_loss_file.txt", "w+")
band_file = open("band_file.txt", "w+")

for index in NO_OF_TESTS:
    siz = 500 * index
    packet_size.append(siz)
    latency, packet_loss = get_latency(size=siz, count=10)
    latency_data.append(float(latency))
    packet_loss_data.append(float(packet_loss))
    bandwidth = siz/float(latency)
    print 'Bandwidth: %s bytes/ms' % bandwidth
    print ''
    size_file.write(str(siz)+'\n')
    lat_file.write(latency+'\n')
    pack_file.write(packet_loss+'\n')
    band_file.write(str(bandwidth)+'\n')

lat_file.close()
pack_file.close()
band_file.close()
size_file.close()
#
# plt.plot(packet_size, latency_data)
# plt.plot(packet_size, packet_loss_data)
# plt.legend(['Latency', 'Packet Loss'], loc='upper left')
# plt.xlabel('Packets Size')
# plt.show()
