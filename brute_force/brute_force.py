from string import printable
import time
import threading

ascii_list = printable
value = 'f8aN'


def brute_force(prev='', total=0, count=0):
    for char in ascii_list:
        print prev + char
        if prev + char == value:
            print prev + char
            print 'Multi thread End time: %s' % (time.time())
            return prev + char

        if count < total:
            c = count + 1
            guess = brute_force(prev + char, total, c)
            if guess is not None:
                return guess


def initiate():
    print 'Multi thread start time: %s' % (time.time())
    for length in range(0, 10):
        t = threading.Thread(target=brute_force, args=('', length))
        t.start()
        # guessed_value = brute_force(total=length)
        # if guessed_value is not None:
        #     print guessed_value
        #     break

# def brute_force2(prev='', total=0, count=0):
#     for char in ascii_list:
#         print prev + char
#         if prev + char == value:
#             return prev + char
#
#         if count < total:
#             c = count + 1
#             guess = brute_force2(prev + char, total, c)
#             if guess is not None:
#                 return guess
#
#
# brute_force2(total=1)


initiate()
