#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list if they are integers.

    Args:
        my_list (list): The list from which elements are printed.
        x (int): The number of elements from my_list to be printed.

    Returns:
        The count of integer elements successfully printed.
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return ret
