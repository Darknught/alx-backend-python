#!/usr/bin/env python3
""" A module that defines a type annotated function sum_mixed_list."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """ Takes a List of integers and floats and return their
    sum as float.
    """
    return sum(mxd_lst)
