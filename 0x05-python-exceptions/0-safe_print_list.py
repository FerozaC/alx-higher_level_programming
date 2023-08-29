#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print a specified number of elements from a list.

    Args:
        my_list (list): The list containing elements to be printed.
        x (int): The desired number of elements from my_list to be printed.

    Returns:
        The count of elements successfully printed.
    """
    elements_printed = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            elements_printed += 1
        except IndexError:
            break
    print("")
    return elements_printed
