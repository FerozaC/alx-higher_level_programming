#!/usr/bin/python3
# 5-no_c.py


def no_c(string):
    """Remove all characters c and C from a string."""
    copy = [x for x in string if x != 'c' and x != 'C']
    return ("".join(copy))
