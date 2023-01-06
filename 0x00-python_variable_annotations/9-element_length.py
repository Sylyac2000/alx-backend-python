#!/usr/bin/env python3
"""
define a function element_length
"""

from typing import List, Tuple, Sequence, Iterable


def element_length(lst:  Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return a list of tuple"""

    return [(i, len(i)) for i in lst]
