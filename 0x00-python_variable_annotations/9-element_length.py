#!/usr/bin/env python3
""" A module that annotate a functions parameters."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ takes in one argument lst which is a list of strings and
    returns the list of tuples where each tuple contaiuns an int
    """
    return [(i, len(i)) for i in lst]
