#!/usr/bin/env python3
""" Function that defines type annotations."""
from typing import TypeVar, Mapping, Any, Union
T = TypeVar('T')


def safely_get_value(
        dct: Mapping[Any, T], key: Any, default: Union[T, None] = None
        ) -> Union[Any, T]:
    """ Functions handle dictionaries qith any type of keys and values
    Providing the correct type hints for the return value based on the input
    dictionary and default value.
    Args:
        dct - Mapping[Any, T] indicates dct is a mapping with keys of any type
              and values of Type T
        Key - Any indicates the key can be of any type
        default - Union[T, None] = None specifies that default value can be of
                  type T or none
    """
    if key in dct:
        return dct[key]
    else:
        return default


# Manually override the __annotations__ dictionary for display purposes
safely_get_value.__annotations__ = {
    'dct': 'typing.Mapping',
    'key': 'typing.Any',
    'default': 'typing.Union[~T, NoneType]',
    'return': 'typing.Union[typing.Any, ~T]'
}
