import subprocess

TAR_BALL_NAME = ''
IP_LIST = []

subprocess.Popen('python setup.py install', stdout=subprocess.PIPE)
subprocess.Popen('python setup.py sdist', stdout=subprocess.PIPE)

password = raw_input("POS root password?")

for ip in IP_LIST:
    command = 'scp %s root@%s:/home/leapset' % (TAR_BALL_NAME, ip)
    print command
