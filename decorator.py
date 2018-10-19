def accumulator(value=0):
    def outer(func):
        def counter(*args, **kwargs):
            print value
            # print count, threshold
            print 'Inside decorator'
            func(*args, **kwargs)

        return counter

    return outer


@accumulator(value='root')
def sample(a, b):
    print '****'
    print a + b
    print '****'


sample(5, 8)


def memo_func(value):
    class Memo(object):
        def __init__(self, func):
            self.count = 0
            self.func = func

        def __call__(self, *args, **kwargs):
            print 'The value is %s' % value
            self.count = self.count + 1
            print 'Inside Memo'
            print 'Count - %s' % self.count
            self.func(*args, **kwargs)
    return Memo


@memo_func(5)
def test_func(a, b):
    print '###'
    print a + b
    print '###'


@memo_func(10)
def sample_test(x):
    print '&&&&&&'
    print x
    print '&&&&&&'


test_func(4, 5)
test_func(4, 6)
test_func(4, 7)
print 'Next function'
sample_test(2)
sample_test(3)
sample_test(4)
sample_test(5)
