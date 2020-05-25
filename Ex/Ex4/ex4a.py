import numpy as np


def find_largest_n(arr, n):
    """
    Find n largest numbers in array arr
    :param arr:     numbers arr
    :param n:       n count
    :return:        n largest numbers
    """
    return np.sort(arr)[-n:]


def find_even_larger_than(arr, val):
    """
    Find all even numbers greater than val in array arr
    :param arr:     numbers array
    :param val:     number
    :return:        all even numbers greater than val
    """
    result = arr[arr > val]
    return result[result % 2 == 0]


def add_prefix(arr, prefix_string):
    """
    Add prefix to all items in array arr
    :param arr:             array
    :param prefix_string:   prefix
    :return:                numpy list of all arr items with prefix_string as prefix
    """
    return [prefix_string + item for item in arr]


def count_string_with_substring(arr, substring):
    """
    Count all substring occasions in array arr
    :param arr:         array
    :param substring:   string
    :return:            count of all substring occasions in arr
    """
    return np.count_nonzero(np.argsort(np.core.defchararray.find(arr, substring)))