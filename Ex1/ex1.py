# 316493758
#1

def min_count1(lst):
    count = 0
    min_value = lst[0]
    for num in lst:
        if num == min_value:
            count += 1
        elif num < min_value:
            count = 1
            min_value = num
    return [min_value, count]


def min_count2(lst):
    return lst.count(min(lst))


def even_filter(num):
    return num % 2 == 0


def string_filter(string_value):
    return isinstance(string_value, str)


def only_even(arg1, arg2):
    return filter(even_filter, range(arg1, arg2))


def only_strings(lst):
    return filter(string_filter, lst)
