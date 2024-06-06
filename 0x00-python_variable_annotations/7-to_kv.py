#!/usr/bin/env python3
""" A Module that defines a type annotated function to_kv."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Takes in two args, first as str and second as int or float
    then returns a tuple
    """
    return (k, float(v ** 2))
