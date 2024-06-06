#!/usr/bin/env python3
""" A module that defines a type annotated function make_multiplier."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Takes in an argument of type float and returns a function
    that multiplies a float by multiplier
    """
    def multiplier_function(x: float) -> float:
        """ The function that will multiply a float by the multiplier."""
        return x * multiplier
    return multiplier_function
