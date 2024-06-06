#!/usr/bin/env python3
""" Using mypy to validate the code below."""
from typing import List, Tuple, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Creates a zoomed-in version of the input list by
    repeating each element 'factor' times.

    Args:
        lst (Tuple): The list of integers to be zoomed in.
        factor (int, optional): The number of times each element
        should be repeated. Defaults to 2.

    Returns:
        List: A new list with each element repeated 'factor' times.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


# Define a list of integers
array: Tuple = [12, 72, 91]

# Create a zoomed-in version of the array with each element repeated twice
zoom_2x = zoom_array(array)

# Create a zoomed-in version of array with each element repeated three times
zoom_3x = zoom_array(array, 3)
