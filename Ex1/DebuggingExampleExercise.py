def change_first_appearance(cur_str, target_char, new_char):
    """
    changes the first appearance of a char to a new char
    :param cur_str: the input string
    :param target_char: the char we search for
    :param new_char:  the char we insert instead of the target char
    :return: a new string with the new char instead of the first appearance of the target char
    """
    first_appearance = cur_str.find(target_char)
    return cur_str[:first_appearance] + new_char + cur_str[first_appearance + 1:]


def iter_l(l):
    """
    ???
    :param l: list of numbers
    :return: ???
    """
    for i in l:
        if i > 3:
            l.append(0)
        print(i)


# exercise1
change_first_appearance('ababab', 'b', 'c')

cur_list = [4, 2, 1]
iter_l(cur_list)
print(cur_list)
