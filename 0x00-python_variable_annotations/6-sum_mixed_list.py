#!/usr/bin/env python3
"""
define a function sum_mixed_list
"""

from typing import List, Union  # in python under 3.10


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return the sum of list of mixed int and float"""

    return sum(mxd_lst)
