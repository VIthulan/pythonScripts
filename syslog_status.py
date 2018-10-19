import logging
import subprocess


def check_syslog_hd_status(caller):
    """
    check_syslog_hd_status
    :param caller: on-demand/reboot
    :return:
    """
    sys_log_hd_status_list = []

    try:
        if caller == 'reboot':
            today_status = check_syslog_hd_status_for_day(checking_day='today')
            yesterday_status = check_syslog_hd_status_for_day(checking_day='yesterday')
            print today_status
            print yesterday_status

            if today_status == 'ERROR' or yesterday_status == 'ERROR':
                return 'ERROR'

            sys_log_hd_status_list = today_status + yesterday_status

        elif caller == 'on-demand':
            today_status = check_syslog_hd_status_for_day(checking_day='today')

            if today_status == 'ERROR':
                return 'ERROR'

            sys_log_hd_status_list = check_syslog_hd_status_for_day(checking_day='today')

        if not sys_log_hd_status_list:
            return ValueDesc()

        # Getting the date_time for the first occurance of yesterday and today
        sys_log_hd_status = sys_log_hd_status_list[0]
        sys_log_hd_status_splitted = sys_log_hd_status.split(' ')
        sys_log_hd_status_date_time = (sys_log_hd_status_splitted[0] + ' '
                                       + sys_log_hd_status_splitted[1] + ' '
                                       + sys_log_hd_status_splitted[2])
        sys_log_hd_status_date_time = sys_log_hd_status_date_time.replace(
            sys_log_hd_status_date_time.split(':')[0], '')

        return ValueDesc(value='Kernel disk read faluires found',
                         desc=sys_log_hd_status_list[0], date=sys_log_hd_status_date_time)
    except Exception as exception:
        logging.exception('Error while checking syslog hd status: %s', exception)
        return ValueDesc(value='ERROR')


def check_syslog_hd_status_for_day(checking_day='today'):
    """
    check_sys_log_hd_status_given_day
    :param checking_day: today/yesterday
    :return: status
    """
    commands = {
        'today': {
            'day': 'date  +"%-d"',
            'month': 'date +"%b"'
        },
        'yesterday': {
            'day': 'date --date="1 days ago" +"%-d"',
            'month': 'date --date="1 days ago" +"%b"'
        }
    }

    try:
        grep_month = p_open_stripped(commands.get(checking_day).get('month'))

        grep_day = p_open_stripped(commands.get(checking_day).get('day'))

        if int(grep_day) < 10:
            space = '  '
        else:
            space = ' '

        grep_day_month = grep_month + space + grep_day
        command = 'zgrep "Unrecovered read error" /var/log/syslog* | grep "' + grep_day_month + '"'
        logging.debug(command)
        sys_log_status_list = p_open_stripped(command).splitlines()

        logging.info('System log hd status %s', sys_log_status_list)

        return sys_log_status_list
    except Exception as exception:
        logging.exception('Error while getting sys log status for %s: %s', checking_day, exception)
        return 'ERROR'


class ValueDesc(object):
    """
    ValueDesc to send diagnosis result
    """

    def __init__(self, value='NULL', desc='', date='NULL'):
        self.VALUE = value
        self.DESCRIPTION = desc
        self.DATE_TIME = date


def p_open_stripped(command):
    """
    Execute subprocess Popen command through this util method
    :param command: Command to execute | string/array
    :return: Output from subprocess with readable format
    """
    try:
        output = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        return output.stdout.read().rstrip().lstrip()
    except Exception as exception:
        logging.exception("Error while running subprocess command: %s", exception)
        return None


print check_syslog_hd_status('reboot').__dict__
