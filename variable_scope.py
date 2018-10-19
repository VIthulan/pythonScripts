import json


def sample(a):
    value = "initial"
    try:
        print 'Setting value'
        if a > 2:
            value = 'greater than 2'
        else:
            value = 'less than 2'
    except Exception as e:
        value = 'Error'

    print value


# x = []
#
# if not len(x):
#     print "inside"


class ValueDesc(object):
    """
    ValueDesc
    """

    def __init__(self, value='NULL', desc='', date='NULL'):
        self.VALUE = value
        self.DESCRIPTION = desc
        self.DATE_TIME = date


# x = ValueDesc(value='this is value', desc='description about value')
# y = json.dumps(x, default=lambda o: o.__dict__)
# print y

def sample_dicts():
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
    print commands.get('yesterday').get('month')


# sample_dicts()


def executor(func):
    try:
        func()
    except Exception as e:
        print e


def actual(a, b):
    def func():
        print a + b
    executor(func=func)

actual(4,7)