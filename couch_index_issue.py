import subprocess
import re
import time
import sys

from threading import Timer

time_pattern = "%Y-%d-%b %H:%M:%S"
given_time = int(time.mktime(time.strptime(('%s 00:00:00' % (time.strftime("%Y/%d/%m"))), "%Y/%d/%m %H:%M:%S")))


def find_pattern_in_logs(path, pattern, start_time=0, end_time=sys.maxint):
    command = 'grep "%s" %s' % (pattern, path)
    try:
        results = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True).stdout.read().rstrip()
        time_stamps = re.findall(r"\d{2}-[A-z][a-z]{2} \d{2}:\d{2}:\d{2}", results)
        print results
        print time_stamps
        # Improvement
        if len(time_stamps) > 0:
            latest_timestamp = time_stamps[len(time_stamps)-1]
            print latest_timestamp
            log_latest_time_epoch = int(
                time.mktime(time.strptime('%s-%s' % (time.strftime("%Y"), latest_timestamp), time_pattern)))
            if start_time <= log_latest_time_epoch <= end_time:
                return True
        return False

        # for time_stamp in reversed(time_stamps):
        #     log_time_epoch = int(time.mktime(time.strptime('%s-%s' % (time.strftime("%Y"), time_stamp), time_pattern)))
        #     print '%s - %s' % (log_time_epoch, time_stamp)
        #     if start_time <= log_time_epoch <= end_time:
        #         print 'Alert after time'
        #         return True
    except Exception as e:
        print e.message
        return False


# start_time = int(time.mktime(time.strptime(('%s 07:00:00' % (time.strftime("%Y/%d/%m"))), "%Y/%d/%m %H:%M:%S")))
# end_time = int(time.mktime(time.strptime(('%s 08:00:00' % (time.strftime("%Y/%d/%m"))), "%Y/%d/%m %H:%M:%S")))
# # print start_time
print find_pattern_in_logs('/home/vithulan/Documents/chrome_debug/Edited/chrome_debug.log', 'preProcessor:PREPROCESSOR_TIME_OUT', int(time.time()) - 60 * 15)
#
# def thread_test():
#     print 'INnoooOnnnnInnoooo'
#
#
# ts = int(time.time())
# print ts
#
# strt = ts-15*60
# print strt
# # t = Timer(60*15, thread_test)
# # t.start()
# print 'emma'
