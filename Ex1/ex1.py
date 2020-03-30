# 316493758
# 1

def min_count1(lst):
    """
     Get minimal value of list, version 1
    :param lst: Numbers list
    :return: Minimal value and its count on the list
    """
    if len(lst) == 0:
        return []
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
    """
    Get minimal value of list, version 2
    :param lst: Numbers list
    :return: Minimal value and its count on the list
    """
    if len(lst) == 0:
        return []
    return [min(lst), lst.count(min(lst))]


def only_even(arg1, arg2):
    """
    Get even numbers between arg1 and arg2
    :param arg1: Number
    :param arg2: Number
    :return: List of the even value between arg1 and arg2
    """

    def even_filter(num):
        """
        Function fo filter
        :param num: Number
        :return:    True if even, else False
        """
        return num % 2 == 0

    return list(filter(even_filter, range(min(arg1, arg2), max(arg1, arg2))))


def only_strings(lst):
    """
    Get a list of the string from lst
    :param lst: List
    :return: List of strings from lst
    """

    def string_filter(obj):
        """
        Function for filter
        :param obj: Object
        :return: True if string, False otherwise
        """
        return isinstance(obj, str)

    return list(filter(string_filter, lst))
