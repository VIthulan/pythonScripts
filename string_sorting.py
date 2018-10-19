# names = ['Amy', 'Harold', 'Yatch']
names = ['Aghay', 'yaala', 'ybaa']


def find_next_word(prev, names_array):
    local_arr = names_array[:]
    reverse_prev = prev[::-1]
    local_arr.append(reverse_prev)
    local_arr.sort()
    index_of_prev = local_arr.index(reverse_prev)
    if index_of_prev == 0:
        return local_arr[1]
    if index_of_prev == len(local_arr) - 1:
        return local_arr[-2]

    return local_arr[index_of_prev + 1]


sorted_array = []
names.sort()
sorted_array.append(names[0])

del names[0]

while names:
    next_word = find_next_word(sorted_array[-1], names)
    sorted_array.append(next_word)
    del names[names.index(next_word)]

print sorted_array
