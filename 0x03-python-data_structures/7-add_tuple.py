#!/usr/bin/python3
# 7-add_tuple.py

def add_tuple(tuple_a=(0, 0), tuple_b=(0, 0)):
    """Add two tuples."""
    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return result
