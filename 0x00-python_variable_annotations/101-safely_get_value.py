#!/usr/bin/env python3
"""safely get value"""


from typing import Union, Any, TypeVar

T = TypeVar('T')

def safely_get_value(dct: dict, key: Any, default: Union[T, None]) -> Union[Any, T]:
    """Return dict value or default"""
    if key in dct:
        return dct[key]
    else:
        return default
    