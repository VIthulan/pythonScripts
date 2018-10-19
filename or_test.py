# val = {}
#
# x = val.get('count') or 0
# print x
#
# val['count'] = 3
#
# y = val.get('count') or 0
# print y

def sample():
    merchant_id = None
    return merchant_id or "merchant id not found"

print sample()