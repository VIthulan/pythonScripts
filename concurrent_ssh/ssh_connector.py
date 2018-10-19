import subprocess
import threading
import time
import random


def connect_to_server():
    SERVER_IP = '184.169.139.115'
    command = 'scp vithulanv@%s:/home/vithulanv/pulse-agent.tar.gz .' % SERVER_IP
    print ''
    print command
    sleep_time = random.uniform(0, 5)
    time.sleep(sleep_time)
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    res = p.communicate()[0].splitlines()
    # print res
    print ''


# connect_to_server()


def initiate():
    for index in range(500):
        print index
        t = threading.Thread(target=connect_to_server)
        t.start()


initiate()
