#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """Prints an integer using the "{:d}" format.

    If a ValueError is caught, it prints a corresponding error message to standard error.

    Args:
        value (int): The integer to be printed.

    Returns:
        Returns True if the integer was successfully printed.
        Returns False if a TypeError or ValueError occurs during printing and prints an error message.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        print("Error: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False
