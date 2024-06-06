#!/usr/bin/env python3
""" Function that defines a duck-typed annotations."""
from typing import Sequence, Optional, Any


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """ Handles any sequence and return the first element if it exists
    or None if the sequence.
    """
    if lst:
        return lst[0]
    else:
        return None
