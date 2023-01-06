#!/usr/bin/env python3
"""
define a function sum_list
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """return the sum of list of float"""
    somme: float = 0
    for elt in input_list:
        somme += elt
    return somme
