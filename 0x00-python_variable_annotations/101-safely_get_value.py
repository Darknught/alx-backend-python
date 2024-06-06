#!/usr/bin/env python3
""" Function that defines type annotations."""
from typing import TypeVar, Mapping, Any, Optional
T = TypeVar('T')


def safely_get_value(
        dct: Mapping[Any, T], key: Any, default: Optional[T] = None
        ) -> Optional[T]:
    """ Functions handle dictionaries qith any type of keys and values
    Providing the correct type hints for the return value based on the input
    dictionary and default value.
    Args:
        dct - Mapping[Any, T] indicates dct is a mapping with keys of any type
              and values of Type T
        Key - Any indicates the key can be of any type
        default - Optional[T] = None specifies that default value can be of
                  type T or none
    """
    if key in dct:
        return dct[key]
    else:
        return default
