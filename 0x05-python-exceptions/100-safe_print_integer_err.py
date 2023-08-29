#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """Prints an integer using the "{:d}" format.
    If ValueError caught, prints corresponding error message to standard error.

    Args:
        value (int): The integer to be printed.

    Returns:
        Returns True if the integer was successfully printed.
        Returns False if TypeError/ ValueError occurs and prints error message.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        print("Error: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False
