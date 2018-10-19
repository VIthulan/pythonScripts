# import subprocess
#
# p = subprocess.Popen(["iperf", '-n200M', '-p19970', '-i1', '-c', '10.10.10.126'], stdout=subprocess.PIPE)
# res = p.communicate()[0].splitlines()
#
# print res[6:]
# print '-----------------------'
# bandwidth_response = res[6:]
# max_throughput = 0
# for bandwidth_result in bandwidth_response:
#     bandwidth = bandwidth_result.split(' ')[-2]
#     print bandwidth
#     max_throughput = float(bandwidth) if float(bandwidth) > max_throughput else max_throughput
#
#
# print 'Maximum throughput: %s MBits/s' % max_throughput
#
#
import logging
import traceback
import sys

LOG_FILENAME = '/home/vithulanv/PycharmProjects/TestProjects/lhc/error.log'
LOG_FILENAME2 = '/home/vithulanv/PycharmProjects/TestProjects/lhc/error2.log'
formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')
handler = logging.FileHandler(LOG_FILENAME, mode='w')
handler.setFormatter(formatter)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

try:
    a = 2 / 0
except Exception as exception:
    with open('log.txt', 'a') as f:
        f.write(str(exception))
        f.write(traceback.format_exc())
