#!/usr/bin/env python3
""" A module that annotate a functions parameters."""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """ takes in one argument lst which is a list of strings and
    returns the list of tuples where each tuple contaiuns an int
    """
    return [(i, len(i)) for i in lst]
