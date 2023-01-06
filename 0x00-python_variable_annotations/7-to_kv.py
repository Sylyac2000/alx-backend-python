#!/usr/bin/env python3
"""
define a function to_kv
"""

from typing import Union, Tuple  # in python under 3.10


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return a tuple"""

    return (k, v ** 2)
