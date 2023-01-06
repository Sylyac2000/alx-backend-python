#!/usr/bin/env python3
"""
define safely_get_value type annotated function
"""

from typing import Any, Mapping, TypeVar, Union
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """type annotated function"""
    if key in dct:
        return dct[key]
    else:
        return default
