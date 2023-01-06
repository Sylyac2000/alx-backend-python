#!/usr/bin/env python3
"""
define a function element_length
"""

from typing import List, Tuple  # in python under 3.10


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """return a list of tuple"""

    return [(i, len(i)) for i in lst]
