#!/usr/bin/python3

def safe_print_integer(value):
    """Print an integer using the "{:d}" format.

    Args:
        value (int): The integer to be printed.

    Returns:
        Returns True if the integer was successfully printed.
        Returns False if a TypeError or ValueError occurs during printing.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
