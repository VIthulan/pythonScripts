# def accumulator(threshold=5, default_response='Processing'):
#     class Memory(object):
#         def __init__(self, func):
#             self.func = func
#             self.count = 0
#             self.results = []
#
#         def __call__(self, *args, **kwargs):
#             results = self.func(*args, **kwargs)
#             self.results.append(results)
#             self.count += 1
#
#             if self.count == threshold and self.results:
#                 status = self.validate()
#                 self.results = []
#                 self.count = 0
#                 return status
#             return default_response
#
#         def validate(self):
#             if isinstance(self.results[0], list):
#                 return self.list_validate()
#             else:
#                 return self.var_validate()
#
#         def list_validate(self):
#             a = None
#             for arr in self.results:
#                 if a is None:
#                     a = arr
#                     continue
#                 a = set(a) - (set(a) - set(arr))
#             if len(set(a)) >= 1:
#                 return list(set(a))
#             return None
#
#         def var_validate(self):
#             if len(set(self.results)) == 1:
#                 return set(self.results).pop()
#             return None
#
#     return Memory


def accumulator(threshold=5, default_response='Processing'):
    def decorator_func(func):
        memory = Memory()

        def receiving_func(*args, **kwargs):
            results = func(*args, **kwargs)
            memory.results.append(results)
            memory.count += 1
            if memory.count == threshold and memory.results:
                status = memory.validate()
                memory.results = []
                memory.count = 0
                return status
            return default_response

        return receiving_func

    return decorator_func


class Memory(object):
    def __init__(self):
        self.count = 0
        self.results = []

    def validate(self):
        if isinstance(self.results[0], list):
            return self.list_validate()
        else:
            return self.var_validate()

    def list_validate(self):
        a = None
        for arr in self.results:
            if a is None:
                a = arr
                continue
            a = set(a) - (set(a) - set(arr))
        if len(set(a)) >= 1:
            return list(set(a))
        return None

    def var_validate(self):
        if len(set(self.results)) == 1:
            return set(self.results).pop()
        return None


@accumulator()
def network_loop(a):
    return a


print network_loop([1, 2, 4, 20, 40])
print network_loop([5, 6, 20, 40])
print network_loop([7, 20, 40])
print network_loop([8, 9, 20, 40])
print network_loop([10, 11, 20, 40])
print network_loop([12, 13, 20, 40])


@accumulator(default_response='Fuck off')
def sampls(b):
    return b


print sampls(4)
print sampls(4)
print sampls(4)
print sampls(4)
print sampls(4)
print sampls(4)
