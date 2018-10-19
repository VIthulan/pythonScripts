import re
import subprocess
import time


def grep_switch_logs(path, *args, **kwargs):
    base = kwargs.get('base') or 'PULSE'
    base_command = "zgrep --with-filename '%s' %s" % (base, path)
    today_date = ''
    switches = '[' + base + ']'
    if kwargs.get('date') is not None:
        try:
            today_date = time.strftime(kwargs.get('date'))
            base_command = base_command + "| grep '%s'" % today_date
        except Exception as exception:
            print 'Exception while getting time from format given'
    if args:
        base_command = base_command + "| grep "
        for key in args:
            base_command = base_command + "'\[%s\]'" % key
            switches = switches + '[' + key + ']'

    print base_command
    out = subprocess.Popen(base_command, stdout=subprocess.PIPE, shell=True)
    out_put = out.stdout.readlines()
    excess = path + ':' + today_date + ' ' + switches
    print 'Out put from command'
    print out_put[0]
    print 'Excess'
    print excess
    print 'After lstrip'
    print out_put[0].replace(excess, '').replace('[', '').replace(']', '')


grep_switch_logs('/home/vithulan/PycharmProjects/TestProjects/log_grep/cpm.log', 'PAYMENT', '20097',
                 date="%Y-%m-%d")
