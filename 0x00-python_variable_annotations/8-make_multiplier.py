#!/usr/bin/env python3
"""
define a function make_multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return a tuple"""

    def multiply(x: float) -> float:
        return x * multiplier
    return multiply
