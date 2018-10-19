import time
import datetime
import subprocess


def transaction_time():
    yesterday = (datetime.date.today() - datetime.timedelta(1)).strftime('%Y-%m-%d')
    yesterday_logs_grep = 'grep "%s" /home/vithulan/PycharmProjects/TestProjects/emv_transaction_time/payment.log | grep "\[AS" ' % yesterday
    logs = subprocess.Popen(yesterday_logs_grep, stdout=subprocess.PIPE,
                            shell=True).stdout.read().splitlines()

    first_transaction = None
    aggregated_time = []
    as1_log_time = None
    for log_line in logs:
        log_time = " ".join(log_line.split(' ', 2)[:2])
        unix_log_time = time.mktime(
            datetime.datetime.strptime(log_time, "%Y-%m-%d %H:%M:%S,%f").timetuple())
        print unix_log_time
        if '[AS1]' in log_line:
            as1_log_time = unix_log_time
            continue

        if as1_log_time is not None and ('[AS2]' in log_line or '[AS3]' in log_line):
            aggregated_time.append(unix_log_time - as1_log_time)
            as1_log_time = None

    print aggregated_time
    print 'Average time'
    average_time = reduce(lambda x, y: x + y, aggregated_time) / len(aggregated_time)
    print average_time


if __name__ == '__main__':
    transaction_time()
