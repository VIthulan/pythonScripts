from threading import Thread, Timer
import subprocess


def sample_method():
    print "hello world111"
    try:
        for num in range(0, 20):
            print "timer1"

        results = subprocess.Popen("ls", stdout=subprocess.PIPE, shell=True).stdout.read().rstrip()
        print "timer 1 - %s" % results
    except Exception as e:
        print e


def sample_method2():
    print "hello world222"
    try:
        for num in range(0, 20):
            print "timer2"

        results = subprocess.Popen("ls", stdout=subprocess.PIPE, shell=True).stdout.read().rstrip()
        print "timer 2 - %s" % results
    except Exception as e:
        print e


def sample_method3():
    print "hello world333"
    try:
        for num in range(0, 20):
            print "timer3"

        results = subprocess.Popen("ls", stdout=subprocess.PIPE, shell=True).stdout.read().rstrip()
        print "timer 3 - %s" % results
    except Exception as e:
        print e


def sample_method4():
    print "hello world444"
    try:
        for num in range(0, 20):
            print "timer4"

        results = subprocess.Popen("ls", stdout=subprocess.PIPE, shell=True).stdout.read().rstrip()
        print "timer 4 - %s" % results
    except Exception as e:
        print e

timer1 = Threading

# timer1 = Timer(3, sample_method)
# timer2 = Timer(3, sample_method)
# timer3 = Timer(3, sample_method)
# timer4 = Timer(3, sample_method)

timer1.start()
timer2.start()
timer3.start()
timer4.start()
