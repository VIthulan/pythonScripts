import datetime
import calendar

#Only for minute < 60
def get_regex_for_time(time_range):
    now = datetime.datetime.now()
    startTime = (datetime.datetime.now() - datetime.timedelta(minutes=time_range))
    regex_for_range = ''
    if startTime.hour == now.hour:
        regex_for_range = str(startTime.day) + '-' + str(calendar.month_abbr[startTime.month])+ ' '+ str(startTime.hour) + ':' + get_regex_for_min(startTime.minute, now.minute)
    else:
        regex_for_range = get_regex_diff_hour(startTime, now)
    print startTime.minute
    print now.minute
    print regex_for_range


def get_regex_region(from_value, to_value):
    return '(' + str(from_value) + ')|(' + str(to_value) + ')'


def get_regex_diff_hour(start_time, now):
    start_regex = str(start_time.day) + '-' + str(calendar.month_abbr[start_time.month]) + ' ' + str(
        start_time.hour) + ':' + get_regex_for_min(start_time.minute, '59')

    end_regex = str(now.day) + '-' + str(calendar.month_abbr[now.month]) + ' ' + str(
        now.hour) + ':' + get_regex_for_min('00', now.minute)
    return get_regex_region(start_regex, end_regex)


def get_regex_for_min(from_value, to_value):
    str_from = str(from_value)
    str_to = str(to_value)
    if len(str_from) < 2:
        str_from = '0'+str_from
    if len(str_to) < 2:
        str_to = '0'+str_to

    if str_from[0] != str_to[0]:
        intermediate = ''
        for i in range(int(str_from[0])+1, int(str_to[0])):
            intermediate += str(i) + '[0-9]|'
        return str_from[0]+'['+str_from[1]+'-9]|'+intermediate + str_to[0]+'[0-'+str_to[1]+']'
    else:
        return str_from[0] + '[' + str_from[1] + '-9]'


get_regex_for_time(30)
