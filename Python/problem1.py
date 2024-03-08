def Joseph(n, k):
    first_list = list(range(n))
    after_list = []
    index = 0
    while len(first_list) > 0:
        index = (index + k - 1) % len(first_list)
        after_list.append(first_list.pop(index))
    return after_list

print(Joseph(7, 3))
